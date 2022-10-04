import numpy as np
import time

data = [1,2,3,4,5,6,7]
data.append(8)
faces = np.array(data)
strat = time.time()
for i in range(len(data)):
    print(faces[i])
#print(sum(data))
print(faces.sum())
print((time.time() - strat) * 1000)