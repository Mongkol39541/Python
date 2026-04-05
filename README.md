# Typhoon ASR Fine-tuning

Fine-tune [Typhoon ASR Realtime](https://huggingface.co/scb10x/typhoon-asr-realtime) (NeMo EncDecRNNTBPE) สำหรับภาษาไทย พร้อม OOV analysis และ WER evaluation

---

## ลำดับการใช้งาน

```
1. pipeline_dataset.sh   prepare wavs + describe stats → บันทึก recommended_params.json
         ↓
2. finetune.sh           อ่าน recommended_params.json → train ทุก subject ต่อเนื่อง
         ↓
3. evaluate.sh           เปรียบเทียบ WER/SER/DER/IER pretrained vs fine-tuned
```

---

## 1. pipeline_dataset.sh

เตรียม dataset และวิเคราะห์สถิติทุก subject แล้ว **บันทึก parameter ที่แนะนำ** โดยอัตโนมัติ

```bash
./pipeline_dataset.sh                     # ทุก subject
./pipeline_dataset.sh SCI64 MAT64 ENG64   # เฉพาะบางวิชา
```

**สิ่งที่ script ทำต่อแต่ละ subject:**

1. **prepare** — แตก wav + สร้าง `manifest.json` จาก HuggingFace Arrow dataset
   (ข้ามถ้ามีอยู่แล้ว)
2. **describe** — วิเคราะห์ duration stats + OOV analysis → `datasets/{SUBJECT}/dataset_report.json`

**ท้ายสุด** คำนวณ parameter ที่แนะนำจาก stats จริงแล้วบันทึกเป็น:

```
datasets/recommended_params.json
```

พร้อมพิมพ์ตารางสรุป:

```
Subject    Hours  modules                 epochs  batch      lr   warmup
------------------------------------------------------------------------
ENG64      42.7h  encoder,decoder,joint       15      8    5e-5      463
SCI64      32.1h  decoder,joint               20     16    1e-4      167
MAT64      90.1h  decoder,joint               10     16    1e-4      440
THA64      86.2h  decoder                     10     16    1e-4      436
SOC64      57.4h  decoder,joint               15     16    1e-4      272
HEA64      23.8h  decoder                     20     16    1e-4      122
ART64      22.1h  decoder                     20     16    1e-4      115
OCC64      20.4h  decoder,joint               20     16    1e-4      105
SCT64      17.3h  decoder,joint               25     16    1e-4      100
HIS64      16.7h  decoder,joint               25     16    1e-4      100
```

**เกณฑ์คำนวณ parameter:**

| Parameter | เกณฑ์ |
|-----------|-------|
| `epochs` | >80h→10, >40h→15, >20h→20, <20h→25 |
| `batch_size` | train encoder→8; mean_sec>5→8; >3→12; ไม่เกิน→16 |
| `lr` | encoder ใน modules→5e-5, อื่นๆ→1e-4 |
| `warmup_steps` | 5% ของ steps ใน epoch แรก (min 100) |

---

## 2. finetune.sh

Train ทุก subject ต่อเนื่อง โดยอ่าน parameter จาก `recommended_params.json` อัตโนมัติ

```bash
./finetune.sh                     # ทุก subject ใน recommended_params.json
./finetune.sh SCI64 MAT64 ENG64   # เฉพาะบางวิชา
```

- ถ้า `manifest.json` ยังไม่มี → prepare dataset ให้อัตโนมัติ
- ถ้ายังไม่ได้รัน `pipeline_dataset.sh` → ใช้ `recommend_params.py` คำนวณ fallback

**โครงสร้าง checkpoint หลังรัน:**

```
checkpoint/
└── {SUBJECT}/
    └── experiments/
        └── thai-finetune-{SUBJECT}/
            └── version_N/
                ├── checkpoints/last-epoch=N.nemo
                └── thai-finetune-{SUBJECT}_final.nemo
```

แต่ละครั้งที่รัน `finetune.sh` ซ้ำบน subject เดิม Lightning จะสร้าง `version_N` ใหม่ — checkpoint เก่าไม่หาย

---

## 3. evaluate.sh

เปรียบเทียบ WER/SER/DER/IER ระหว่าง pretrained กับ fine-tuned model

```bash
./evaluate.sh                               # latest checkpoint ทุก subject
./evaluate.sh SCI64 MAT64                   # latest checkpoint เฉพาะบางวิชา
./evaluate.sh SCI64=/path/to/model.nemo     # ระบุ checkpoint เฉพาะ run
```

**กรณีเทรนซ้ำหลายครั้ง** script จะแสดง checkpoint ทั้งหมดที่มีและเลือก latest อัตโนมัติ:

```
  Available checkpoints (3):
    → checkpoint/SCI64/.../version_2/thai-finetune-SCI64_final.nemo  [selected: latest]
      checkpoint/SCI64/.../version_1/thai-finetune-SCI64_final.nemo
      checkpoint/SCI64/.../version_0/thai-finetune-SCI64_final.nemo
  Tip: use ./evaluate.sh SCI64=/path/to/model.nemo to pick one
```

ถ้าต้องการ eval run เก่า ให้ copy path แล้วระบุตรงๆ:

```bash
./evaluate.sh SCI64=checkpoint/SCI64/experiments/.../version_0/thai-finetune-SCI64_final.nemo
```

**Output บันทึกแยก timestamp** ไม่ทับกันทุกครั้งที่รัน:

```
eval_output/
└── {SUBJECT}/
    └── 20260405_143022/         ← timestamp ของแต่ละ eval run
        ├── eval_results.json
        ├── references.csv
        ├── predictions_pretrain.csv
        └── predictions_finetune.csv
```

**ตัวอย่าง output:**

```
  Metric    Pretrained    Fine-tuned      Δ
  ────────  ────────────  ────────────  ──────
  WER           18.42%         9.17%    +9.25%
  SER           10.13%         5.02%    +5.11%
  DER            5.21%         2.84%    +2.37%
  IER            3.08%         1.31%    +1.77%

  WER relative improvement : +50.22%
  Verdict                  : Fine-tuned BETTER
```

---

## โครงสร้างโปรเจกต์

```
typhoon-asr/
├── scripts/
│   ├── prepare_dataset.py     แปลง HuggingFace Arrow dataset → wav + manifest
│   ├── describe_dataset.py    สถิติ duration + OOV analysis → dataset_report.json
│   ├── summarize_subjects.py  สรุป samples + ชั่วโมงทุก subject
│   ├── recommend_params.py    คำนวณ parameter จาก dataset stats (ใช้เป็น fallback)
│   ├── finetune.py            fine-tune โมเดล พร้อม tracking RAM/time/W&B
│   └── evaluate.py            เปรียบเทียบ WER/SER/DER/IER
├── datasets/
│   ├── subjects_summary.json       สรุป samples + hours ทุก subject
│   ├── recommended_params.json     parameter ที่แนะนำ (สร้างโดย pipeline_dataset.sh)
│   └── {SUBJECT}/
│       ├── train/manifest.json
│       ├── validation/manifest.json
│       ├── test/manifest.json
│       └── dataset_report.json     stats + OOV analysis
├── checkpoint/
│   └── {SUBJECT}/experiments/thai-finetune-{SUBJECT}/version_N/
│       ├── checkpoints/last-epoch=N.nemo
│       └── thai-finetune-{SUBJECT}_final.nemo
├── eval_output/
│   └── {SUBJECT}/{TIMESTAMP}/
│       ├── eval_results.json
│       ├── references.csv
│       ├── predictions_pretrain.csv
│       └── predictions_finetune.csv
├── pipeline_dataset.sh     ← step 1: prepare + describe + save recommended_params.json
├── finetune.sh             ← step 2: train (อ่านจาก recommended_params.json)
└── evaluate.sh             ← step 3: eval (auto-find latest หรือระบุ checkpoint)
```

---

## โครงสร้าง Dataset ที่รองรับ

`prepare_dataset.py` รับ dataset ในรูปแบบ **HuggingFace Arrow** (`save_to_disk`)

### Columns ที่ต้องมี

| Column | Type | หมายเหตุ |
|--------|------|----------|
| `audio` | `Audio` | bytes หรือ path |
| `text` หรือ `text_clean` | `string` | ถ้ามีทั้งคู่ใช้ `text_clean` ก่อน |
| `duration` | `float` | หน่วยวินาที |
| `subject` | `string` | ใช้กับ `--subject` เพื่อ filter เช่น `SCI64` |

### Dataset ที่ใช้ใน project นี้ (DLTV)

```
dltv_dataset_2024-01-26-verify/
├── train/        659,948 samples   ≈ 409 ชั่วโมง
├── validation/    73,328 samples   ≈  45 ชั่วโมง
└── test/          81,476 samples   ≈  50 ชั่วโมง

subjects: ART64, ENG64, HEA64, HIS64, MAT64,
          OCC64, SCI64, SCT64, SOC64, THA64
```
