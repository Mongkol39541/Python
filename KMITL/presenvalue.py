import time

def SequencesV1(num):
    total = 0
    for loop in range(1, num + 1):
        total += loop
    return total

def SequencesV2(num):
    total = (num / 2) * (2 + (num - 1) * 1)
    return total

num = int(input())

startV1 = time.time()
print("Answer Of SequencesV1 : ", int(SequencesV1(num)))
print("Time Of SequencesV1 : ", (time.time() - startV1) * 1000)

startV2 = time.time()
print("Answer Of SequencesV2 : ", int(SequencesV2(num)))
print("Time Of SequencesV2 : ", (time.time() - startV2) * 1000)