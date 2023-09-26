import cv2

cap = cv2.VideoCapture("คงจะดีนะ.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame[:, ::-1, :])
    if cv2.waitKey(30) == ord('q') or not ret:
        break
cap.release()