# Typhoon ASR Fine-tuning

Fine-tune โมเดล [Typhoon ASR Realtime](https://huggingface.co/scb10x/typhoon-asr-realtime) (NeMo EncDecRNNTBPE) สำหรับภาษาไทย พร้อม OOV analysis และ WER evaluation

---

## โครงสร้างโปรเจกต์

```
typhoon-asr/
├── scripts/
│   ├── summarize_subjects.py  สรุป samples + ชั่วโมงของทุก subject ใน dataset
│   ├── prepare_dataset.py     แปลง HuggingFace Arrow dataset → wav + manifest
│   ├── describe_dataset.py    สถิติ dataset และ OOV analysis
│   ├── create_manifest.py     สร้าง NeMo manifest จาก audio + transcripts
│   ├── finetune.py            fine-tune โมเดล พร้อม tracking RAM/time
│   └── evaluate.py            เปรียบเทียบ WER/SER/DER/IER
├── datasets/
│   └── {SUBJECT}/             เช่น SCI64/, MAT64/
│       ├── train/
│       │   ├── wavs/          ไฟล์เสียง .wav
│       │   └── manifest.json  NeMo manifest
│       ├── validation/
│       │   ├── wavs/
│       │   └── manifest.json
│       └── test/
│           ├── wavs/
│           └── manifest.json
├── checkpoint/                tokenizer + experiment logs + model weights
│   └── experiments/
│       └── <run_name>/
│           └── <timestamp>/
│               ├── checkpoints/
│               │   └── last-<epoch>.nemo
│               └── <run_name>_final.nemo
├── eval_output/               ผลการ evaluate
│   ├── eval_results.json
│   ├── references.csv
│   ├── predictions_pretrain.csv
│   └── predictions_finetune.csv
├── summarize_subjects.sh
├── prepare_dataset.sh
├── describe_dataset.sh
├── create_manifest.sh
├── finetune.sh
└── evaluate.sh
```

---

## โครงสร้าง Dataset ที่รองรับ

`prepare_dataset.py` รับ dataset ในรูปแบบ **HuggingFace Arrow** (สร้างด้วย `save_to_disk`) โดยมีข้อกำหนดดังนี้

### โครงสร้างโฟลเดอร์

```
my_dataset/
├── train/
│   ├── dataset.arrow
│   ├── dataset_info.json
│   └── state.json
├── validation/
│   ├── dataset.arrow
│   ├── dataset_info.json
│   └── state.json
├── test/
│   ├── dataset.arrow
│   ├── dataset_info.json
│   └── state.json
└── dataset_dict.json
```

สร้างจาก Python ด้วย:

```python
dataset_dict.save_to_disk("/path/to/my_dataset")
# โหลดกลับด้วย
dataset = load_from_disk("/path/to/my_dataset")
```

### Columns ที่ต้องมี

| Column | Type | ความหมาย |
|---|---|---|
| `audio` | `Audio` | ไฟล์เสียง — เก็บเป็น bytes หรือ path ก็ได้ |
| `text` หรือ `text_clean` | `string` | transcript — ถ้ามีทั้งคู่จะใช้ `text_clean` ก่อน |
| `duration` | `float` | ความยาวเสียงหน่วยวินาที |

### Columns เสริม (optional)

| Column | Type | ความหมาย |
|---|---|---|
| `subject` | `string` | ใช้กับ `--subject` เพื่อ filter เฉพาะกลุ่ม เช่น `SCI64` |
| `class` | `string` | ระดับชั้น เช่น `P4`, `M1` |
| `audio_file` | `string` | ชื่อไฟล์ต้นทาง |

### รูปแบบ Audio ที่รองรับ

**แบบที่ 1 — เก็บ bytes ใน Arrow (แนะนำ)**

```python
from datasets import Audio
dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))
# audio column จะมี {"array": ..., "sampling_rate": 16000}
```

**แบบที่ 2 — เก็บ path อย่างเดียว (ไม่ embed)**

```python
dataset = dataset.cast_column("audio", Audio(decode=False))
# audio column จะมี {"path": "/abs/path/to/file.wav", "bytes": None}
# ต้องมีไฟล์จริงอยู่ที่ path นั้น
```

> `prepare_dataset.py` ใช้ `decode=False` เพื่อความเร็ว แล้ว decode เองด้วย `soundfile`

### ตัวอย่างสร้าง Dataset จาก CSV + ไฟล์เสียง

```python
import pandas as pd
import soundfile as sf
import io
from datasets import Dataset, DatasetDict, Audio

# สมมติมี CSV แบบนี้:
# filename, text, duration
# file001.wav, สวัสดีครับ, 1.23
# file002.wav, วันนี้อากาศดี, 2.10

df = pd.read_csv("transcripts.csv")

def load_sample(row):
    audio_path = f"/path/to/wavs/{row['filename']}"
    return {
        "audio": audio_path,
        "text": row["text"],
        "duration": row["duration"],
        "subject": "CUSTOM",   # optional
    }

rows = [load_sample(r) for _, r in df.iterrows()]
dataset = Dataset.from_list(rows).cast_column("audio", Audio(sampling_rate=16000))

# แบ่ง split เอง
split = dataset.train_test_split(test_size=0.1, seed=42)
dataset_dict = DatasetDict({
    "train":      split["train"],
    "validation": split["test"],
    "test":       split["test"],   # หรือใช้ test set แยกต่างหาก
})

dataset_dict.save_to_disk("/path/to/my_dataset")
```

### ตัวอย่างโครงสร้าง dataset ที่ใช้ใน project นี้ (DLTV)

```
dltv_dataset_2024-01-26-verify/
├── train/        659,948 samples   ≈ 328 ชั่วโมง
├── validation/    73,328 samples   ≈  36 ชั่วโมง
└── test/          81,476 samples   ≈  40 ชั่วโมง

columns: audio, text, text_clean, duration, subject, class,
         audio_file, file_name_only, start, end, full_path

subjects: ART64, ENG64, HEA64, HIS64, MAT64,
          OCC64, SCI64, SCT64, SOC64, THA64
```

project นี้ใช้เฉพาะ subject `SCI64` ซึ่งมี:

| split | samples | ชั่วโมง |
|---|---|---|
| train | 53,565 | ~26.6 h |
| validation | 5,947 | ~2.9 h |
| test | 6,609 | ~3.3 h |

---

## ลำดับการใช้งาน

```
1. summarize_subjects     ดูข้อมูลรวมทุก subject → ยืนยัน hours + train_modules
         ↓
2. finetune               prepare (อัตโนมัติถ้ายังไม่มี) + train ทุกวิชาต่อเนื่อง
         ↓
3. evaluate               เปรียบเทียบ WER/SER/DER/IER + บันทึก CSV
```

> `prepare_dataset.sh` และ `describe_dataset.sh` ใช้ถ้าต้องการดู/เตรียม dataset ของวิชาใดวิชาหนึ่งแยกก่อน
> `create_manifest.sh` ใช้เฉพาะกรณีต้องการ regenerate manifest โดยไม่ extract wav ใหม่

---

## 1. สรุปข้อมูลทุก Subject

ดูจำนวน samples และชั่วโมงของ **ทุก subject** ใน Arrow dataset ก่อน เพื่อตัดสินใจว่าจะ fine-tune subject ไหน และควรใช้ `--train_modules` อะไร

```bash
bash summarize_subjects.sh
```

**ตัวอย่าง output:**

```
──────────────────────────────────────────────────────────────────────────────
Subject     train samples  train hours  val samples   val hours  test samples  test hours  total hours
──────────────────────────────────────────────────────────────────────────────
MAT64              71,234        35.2h        7,915       3.9h        8,794       4.4h       43.5h
SOC64              68,901        34.1h        7,656       3.8h        8,512       4.2h       42.1h
ENG64              65,432        32.3h        7,270       3.6h        8,079       4.0h       39.9h
THA64              61,209        30.3h        6,801       3.4h        7,556       3.7h       37.4h
HIS64              58,774        29.1h        6,530       3.2h        7,256       3.6h       35.9h
SCI64              53,565        26.6h        5,947       2.9h        6,609       3.3h       32.8h
SCT64              51,023        25.3h        5,669       2.8h        6,296       3.1h       31.2h
OCC64              49,887        24.7h        5,543       2.7h        6,159       3.0h       30.4h
HEA64              47,234        23.4h        5,248       2.6h        5,832       2.9h       28.9h
ART64              32,689        16.2h        3,632       1.8h        4,037       2.0h       20.0h
──────────────────────────────────────────────────────────────────────────────
TOTAL             659,948       277.1h       73,211      30.7h       81,130      34.2h      342.0h
──────────────────────────────────────────────────────────────────────────────
```

**แนะนำ `--train_modules` ตามจำนวนชั่วโมงและลักษณะวิชา:**

| Subject | วิชา | ชั่วโมง (approx) | แนะนำ | เหตุผล |
|---|---|---|---|---|
| **ENG64** | ภาษาอังกฤษ | ~32h | `encoder,decoder,joint` | ครูออกเสียงอังกฤษปน → acoustic ต่างจาก pretrain |
| **SCI64** | วิทยาศาสตร์ | ~27h | `decoder,joint` | loanword เยอะ OOV สูง |
| **SCT64** | วิทย์เทคโนโลยี | ~25h | `decoder,joint` | คล้าย SCI64 |
| **MAT64** | คณิตศาสตร์ | ~35h | `decoder,joint` | ตัวเลข/สมการ pattern ต่าง |
| **HIS64** | ประวัติศาสตร์ | ~29h | `decoder,joint` | proper noun ชื่อบุคคล/สถานที่เยอะ |
| **SOC64** | สังคมศึกษา | ~34h | `decoder,joint` | ชื่อประเทศ ภูมิศาสตร์ |
| **OCC64** | การงานอาชีพ | ~25h | `decoder,joint` | คำเทคนิคเฉพาะสาขา |
| **HEA64** | สุขศึกษา | ~23h | `decoder` | คำสุขภาพ ไม่ซับซ้อนมาก |
| **THA64** | ภาษาไทย | ~30h | `decoder` | acoustic ปกติ แค่ปรับ language pattern |
| **ART64** | ศิลปะ | ~16h | `decoder` | vocabulary ทั่วไป dataset เล็กสุด |

> ตัวเลขชั่วโมงข้างบนเป็นค่าโดยประมาณ ให้รัน `summarize_subjects.sh` เพื่อดูตัวเลขจริง

---

## 2. เตรียม Dataset

แปลง HuggingFace Arrow dataset เป็นไฟล์ `.wav` และ `manifest.json` สำหรับ NeMo

```bash
bash prepare_dataset.sh
```

**ปรับ config ใน `prepare_dataset.sh`:**

| ตัวแปร | ความหมาย | ค่าเริ่มต้น |
|---|---|---|
| `SUBJECT` | subject ที่ต้องการ filter | `SCI64` |
| `DATASET_PATH` | path ของ Arrow dataset | dltv_dataset_2024-01-26-verify |
| `--subject` | filter ตาม subject (ละไว้ = ทั้งหมด) | `SCI64` |
| `--splits` | splits ที่ต้องการ export | `train,validation,test` |

**ตัวอย่างการรันโดยตรง:**

```bash
# export เฉพาะ MAT64
python scripts/prepare_dataset.py \
    --dataset_path /project/.../dltv_dataset_2024-01-26-verify \
    --output_dir   datasets/MAT64 \
    --subject      MAT64 \
    --splits       train,validation,test

# export ทุก subject (ไม่ filter)
python scripts/prepare_dataset.py \
    --dataset_path /project/.../dltv_dataset_2024-01-26-verify \
    --output_dir   datasets/ALL \
    --splits       train,validation,test
```

**Output:**
```
[train]      SCI64: 53,565 samples  → datasets/SCI64/train/manifest.json
[validation] SCI64:  5,947 samples  → datasets/SCI64/validation/manifest.json
[test]       SCI64:  6,609 samples  → datasets/SCI64/test/manifest.json
```

---

## 3. ดูสถิติ Dataset และ OOV Analysis

วิเคราะห์ dataset และหาคำที่ tokenizer แตกออกเป็นหลาย subword (OOV-like words)

```bash
bash describe_dataset.sh
```

**ตัวอย่างการรันโดยตรง:**

```bash
python scripts/describe_dataset.py \
    --data_dir       datasets/SCI64 \
    --model          /project/.../typhoon-asr-realtime.nemo \
    --splits         train,validation,test \
    --oov_top        50 \
    --min_word_freq  2       # ไม่นับคำที่ปรากฏแค่ครั้งเดียว
```

**ตัวอย่าง output:**

```
======================================================================
                        DATASET STATISTICS
======================================================================

[train]
  samples      : 53,565
  total hours  : 26.58 h
  duration     : mean=1.79s  std=0.57s  min=1.00s  max=20.00s

[validation]
  samples      : 5,947
  total hours  :  2.95 h
  duration     : mean=1.78s  std=0.56s  min=1.00s  max=19.80s

[test]
  samples      : 6,609
  total hours  :  3.28 h
  duration     : mean=1.79s  std=0.57s  min=1.00s  max=18.40s

──────────────────────────────────────────────────────────────────────
VOCABULARY (combined across all splits)
  unique words      : 12,431
  unique characters : 87
  total words       : 482,104

  Top 20 most frequent words:
    ของ                  18,432
    และ                  15,219
    ...

──────────────────────────────────────────────────────────────────────
TOKENIZER OOV ANALYSIS
  Tokenizer vocab size: 2,048
  Words fragmented into >1 BPE token : 8,214 / 12,431 (66.1%)

  Top 50 most-fragmented words (ratio = tokens/chars):
  Word                      Freq  Tokens  Chars  Ratio  Decoded
  ───────────────────────── ────── ────── ───── ────── ────────
  ไมโทคอนเดรียล               14       9      7   1.29  ไมโทคอนเดรียล
  โฟโตซินเทสิส                 8      10      8   1.25  โฟโตซินเทสิส
```

> **หมายเหตุ:** ratio = จำนวน BPE tokens / จำนวน characters — ยิ่งสูงยิ่งถูก tokenizer แตกมาก คำที่ ratio สูงคือคำที่ tokenizer ไม่ค่อยคุ้นเคย (rare หรือ domain-specific)

---

## 4. สร้าง Manifest (กรณี regenerate)

ใช้เมื่อมีไฟล์เสียงอยู่แล้วและต้องการสร้าง manifest ใหม่

```bash
bash create_manifest.sh
```

**ตัวอย่างการรันโดยตรง:**

```bash
# จาก CSV
python scripts/create_manifest.py \
    --audio_dir   datasets/SCI64/train/wavs \
    --transcripts datasets/SCI64/train/transcripts_manifest.csv \
    --output      datasets/SCI64/train/manifest.json

# จาก JSON
python scripts/create_manifest.py \
    --audio_dir   datasets/SCI64/train/wavs \
    --transcripts datasets/SCI64/train/transcripts.json \
    --output      datasets/SCI64/train/manifest.json
```

**รูปแบบ transcripts ที่รองรับ:**

| รูปแบบ | columns / โครงสร้าง |
|---|---|
| `.csv` | `filename`, `transcription` |
| `.json` | `{"filename": "text", ...}` หรือ `[{"filename": ..., "text": ...}]` |
| `.txt` | หนึ่งบรรทัดต่อหนึ่งไฟล์เสียง (เรียงตามชื่อไฟล์) |
| โฟลเดอร์ | ไฟล์ `.txt` แต่ละไฟล์ชื่อเดียวกับ audio |

---

## 5. Fine-tune

```bash
bash finetune.sh
```

script จะ loop ทุก subject ต่อเนื่องอัตโนมัติ:
- ถ้า manifest ยังไม่มี → `prepare_dataset` ให้ก่อน
- ใช้ `--train_modules` ที่เหมาะสมของแต่ละวิชา
- แยก checkpoint ต่าง subject: `checkpoint/{SUBJECT}/`

**subject และ train_modules ที่ใช้:**

| Subject | วิชา | train_modules | เหตุผล |
|---|---|---|---|
| ENG64 | ภาษาอังกฤษ | `encoder,decoder,joint` | ครูออกเสียงอังกฤษปน → acoustic ต่าง |
| SCI64 | วิทยาศาสตร์ | `decoder,joint` | loanword วิทย์ OOV สูง |
| SCT64 | วิทย์เทคโนโลยี | `decoder,joint` | คล้าย SCI64 |
| MAT64 | คณิตศาสตร์ | `decoder,joint` | ตัวเลข/สมการ pattern ต่าง |
| HIS64 | ประวัติศาสตร์ | `decoder,joint` | proper noun เยอะ |
| SOC64 | สังคมศึกษา | `decoder,joint` | ชื่อประเทศ ภูมิศาสตร์ |
| OCC64 | การงานอาชีพ | `decoder,joint` | คำเทคนิคเฉพาะสาขา |
| HEA64 | สุขศึกษา | `decoder` | ศัพท์สุขภาพ ไม่ซับซ้อนมาก |
| THA64 | ภาษาไทย | `decoder` | acoustic ปกติ แค่ปรับ language pattern |
| ART64 | ศิลปะ | `decoder` | vocabulary ทั่วไป dataset เล็กสุด |

**ปรับค่าได้ใน `finetune.sh`:**

```bash
EPOCHS=50
BATCH_SIZE=8
LR=1e-4
```

ถ้าต้องการ train แค่บางวิชา ตัดออกจาก array `SUBJECTS`:
```bash
SUBJECTS=("SCI64" "MAT64" "ENG64")
```

**โครงสร้าง checkpoint หลังรันครบ:**
```
checkpoint/
├── ENG64/experiments/thai-finetune-ENG64/.../thai-finetune-ENG64_final.nemo
├── SCI64/experiments/thai-finetune-SCI64/.../thai-finetune-SCI64_final.nemo
├── MAT64/...
└── ...
```

**Arguments สำคัญ:**

| Argument | ความหมาย | ค่าเริ่มต้น |
|---|---|---|
| `--model_name` | path หรือชื่อโมเดลบน NGC | required |
| `--train_manifest` | manifest สำหรับ train | required |
| `--val_manifest` | manifest สำหรับ validation | optional |
| `--data_dir` | ที่เก็บ tokenizer + checkpoints | `./checkpoint` |
| `--epochs` | จำนวน epoch | `50` |
| `--batch_size` | batch size | `16` |
| `--lr` | learning rate | `1e-3` |
| `--train_modules` | โมดูลที่ train: `encoder`, `decoder`, `joint`, `all` | `all` |
| `--change_vocabulary` | สร้าง tokenizer ใหม่จาก training data | flag (off) |
| `--vocab_size` | vocab size ถ้า change_vocabulary | `2048` |
| `--resume_from_checkpoint` | path ของ `.ckpt` สำหรับ resume | optional |
| `--wandb_project` | ชื่อ W&B project | `nemo_asr_finetune` |
| `--wandb_name` | ชื่อ W&B run | auto-generated |

**ท้าย training จะแสดง:**

```
============================================================
TRAINING COMPLETE
  Time elapsed    : 02h 14m 33s
  CPU RAM (after) : 18.42 GB
  GPU RAM (after) :  6.31 GB
  GPU RAM (peak)  : 11.87 GB
============================================================
```

**Checkpoint และ Final model** จะถูก save ที่:
```
checkpoint/experiments/<run_name>/<timestamp>/
├── checkpoints/
│   └── last-<epoch>.nemo
└── <run_name>_final.nemo       ← ใช้สำหรับ inference / evaluate
```

---

## 6. Evaluate WER / SER / DER / IER

เปรียบเทียบ error rates ระหว่าง pretrained กับ fine-tuned model

```bash
bash evaluate.sh
```

> **หมายเหตุ:** แก้ไข path `FINETUNED` ใน `evaluate.sh` ให้ตรงกับ run ที่ต้องการก่อนรัน

**ตัวอย่างการรันโดยตรง:**

```bash
python scripts/evaluate.py \
    --pretrained_model /project/.../typhoon-asr-realtime.nemo \
    --finetuned_model  checkpoint/experiments/<run>/<timestamp>/<run>_final.nemo \
    --test_manifest    datasets/SCI64/test/manifest.json \
    --batch_size       8 \
    --output_dir       eval_output \
    --show_samples     5

# ทดสอบแค่ 200 ตัวอย่างก่อน
python scripts/evaluate.py \
    --pretrained_model /project/.../typhoon-asr-realtime.nemo \
    --finetuned_model  checkpoint/experiments/.../final.nemo \
    --test_manifest    datasets/SCI64/test/manifest.json \
    --num_samples      200
```

**Arguments:**

| Argument | ความหมาย | ค่าเริ่มต้น |
|---|---|---|
| `--pretrained_model` | path หรือชื่อ pretrained model | required |
| `--finetuned_model` | path ของ fine-tuned `.nemo` | required |
| `--test_manifest` | manifest สำหรับ test | required |
| `--batch_size` | batch size สำหรับ inference | `8` |
| `--num_samples` | จำกัดจำนวน sample (ทดสอบเร็ว) | ทั้งหมด |
| `--output_dir` | โฟลเดอร์บันทึก JSON + CSV | optional |
| `--show_samples` | จำนวน sample ที่แสดง prediction | `5` |

**ตัวอย่าง output:**

```
  Metric    Pretrained    Fine-tuned      Δ (abs)
  ────────  ────────────  ────────────  ──────────
  WER           18.42%         9.17%      +9.25%
  SER           10.13%         5.02%      +5.11%
  DER            5.21%         2.84%      +2.37%
  IER            3.08%         1.31%      +1.77%

  WER relative improvement : +50.22%
  Verdict                  : Fine-tuned BETTER
```

ผลจะถูกบันทึกที่ `eval_output/`:

```
eval_output/
├── eval_results.json          ← metrics ครบทุกตัว
├── references.csv             ← reference transcripts
├── predictions_pretrain.csv   ← pretrained model hypotheses
└── predictions_finetune.csv   ← fine-tuned model hypotheses
```

แต่ละ CSV มี columns: `message`, `agent_id` (= 0), `message_id` (= 0, 1, 2, ...)
