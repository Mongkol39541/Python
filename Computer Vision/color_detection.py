import cv2
import numpy as np
import matplotlib.pyplot as plt

A = cv2.imread('coins.png')
cv2.imshow('A',A)
plt.imshow(A)

tol = 30
color = np.array([30, 30, 50])
plt.imshow(A[:, :, ::-1])
plt.show()

mask = cv2.inRange(A, color-tol, color+30)
Amask = cv2.bitwise_and(A, A, mask=mask)
cv2.imshow('mask', mask)
cv2.imshow('Amask', Amask)
cv2.waitKey()
cv2.imwrite('mask.png', mask)
cv2.imwrite('Amask.png', Amask)