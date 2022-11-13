# ถ้าต้องการใช้เวลาน้อยไม่ควรใข้ kNN เพราะ เมื่อมีข้อมูลมา ค่าระยะห่างยูคลิดจะไม่ส่งผลต่อการประมวลผล

import numpy as np

def kNN(Xtrain, Ytrain, Xtest, k=1):
    Ytest = []
    for x in Xtest:
        d = np.sqrt(np.sum(np.dot(np.dot(Xtrain - x, (Xtrain - x).T), ((Xtrain - x) ** 2) / (len(Xtest ) - 1)), axis=1))
        idx = np.argsort(d)
        (values, counts) = np.unique(Ytrain[idx[:k]], return_counts=True)
        ind = np.argmax(counts)
        Ytest.append(values[ind])
    return Ytest

# เราสามารถเอามาใช้ร่วมกันได้
# 1. CNN นำมาลดข้อมูลชุดตัวอย่างที่ใกล้เคียงกัน แต่ให้ผลลัพธ์ต่างกันออกไป
# 2. K-d Tree ใช้มิติในการลดข้อมูลชุดตัวอย่าง แบ่งออกมาเป็นมิติให้ข้อมูลชุดตัวอย่างที่ใกล้เคียงและให้ผลลัพธ์ที่เหมือนกัน มารวมเป็นชุดเดียวกัน
# 3. LSH เมื่อข้อมูลที่มีมิติมาก เราสามารถใช้ LSH มาลดมิติในการคำนวณให้น้อยลงด้วย Vector