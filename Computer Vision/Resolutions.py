import numpy as np
import cv2
import matplotlib.pyplot as plt

def image2bitplane(img):
    bp = []
    for c in range(img.shape[2]):
        for i in range(8):
            bp.append(img[:, :, c] // 2 ** i % 2)
    return np.array(bp)

def bitplane2image(bp):
    img = np.zeros((bp[0].shape[0], bp[0].shape[1], 3))
    for b in range(len(bp)):
        img[:, :, b//8] = img[:, :, b//8] + (bp[b] + (bp[b] * 2**(b % 8)))
    return np.uint8(img)

im = cv2.imread('bell.jpg')[:, :, ::-1]
bp = image2bitplane(im)

idx = np.r_[4:8, 12:16, 20:24]
idx_ans = np.r_[0:4, 8:12, 16:20][::-1]

bp_ans = np.zeros_like(bp)
bp_ans[idx] = bp[idx_ans]
ans = bitplane2image(bp_ans)
plt.subplot(1, 2, 1)
plt.imshow(im)
plt.subplot(1, 2, 2)
plt.imshow(ans)
plt.show()