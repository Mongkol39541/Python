import cv2
import numpy as np

cap = cv2.VideoCapture('คงจะดีนะ.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vdo_writer = cv2.VideoWriter('out.mp4', fourcc, 30, (426, 240))
n_buffer = 10
buffer = None
iframe = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if buffer is None:
        buffer = np.zeros((n_buffer, *gray.shape))
    buffer[iframe % n_buffer] = gray
    if iframe >= n_buffer:
        # M = np.mean(buffer, axis=0)
        M = np.median(buffer, axis=0)
        diff = cv2.absdiff(gray, np.uint8(M))
        fg = np.uint8((diff > .4 * np.max(diff)) * 255)
        cv2.imshow('fg', fg)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q') or not ret:
        break
    iframe += 1
    vdo_writer.write(frame)

vdo_writer.release()