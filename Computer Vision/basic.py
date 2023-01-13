import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# im_shape = 480, 640, 3
# im = (np.random.rand(*im_shape) * 255).astype(np.uint8)
# plt.imshow(im)
# plt.show()

thai = np.ones((6, 9, 3))
thai[[0, -1], :, 1:] = 0
thai[2:4, :, :2] = 0
# plt.imshow(thai)
# plt.show()

# cv2.imshow('Thai', cv2.resize(thai, None, fx=100, fy=100))
# cv2.waitKey()

japan = np.ones((600, 900, 3))
r = 3/5/2 * japan.shape[0]
c = [i//2 for i in japan.shape[:2]]
for i in range(japan.shape[0]):
    for j in range(japan.shape[1]):
        if (i - c[0])**2 + (j - c[1])**2 <= r**2:
            japan[i, j, 1:] = 0
# plt.imshow(japan)
# plt.axis('off')
# plt.show()

pui = plt.imread('puimek.jpg')
# plt.imshow(im)
# plt.show()

# im = Image.open('puimek.jpg')
# im = np.array(im)
# plt.imshow(im)
# plt.show()

# im = cv2.imread('puimek.jpg')
# cv2.imshow('im', im)
# cv2.waitKey()

# im_copy = im.copy()
# for i in range(im.shape[0]):
#     for j in range(im.shape[1]):
#         im[i, j, 0] = im_copy[i, j, 2]
#         im[i, j, 2] = im_copy[i, j, 0]
# plt.imshow(im)
# plt.show()

# cv2.imwrite('Japan.png', np.uint8(japan[:, :, ::-1] * 255))

# im_thai = Image.fromarray(np.uint8(thai*255))
# im_thai.save('Thai.jpg')

# im = Image.fromarray(np.uint8(pui*255))
# im2 = Image.fromarray(np.uint8(255 - pui*255))
# im.save('Puimek.gif', save_all=True, append_images=[im2, im]*20)

