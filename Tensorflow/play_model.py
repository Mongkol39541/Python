import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('image.jpg')

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = hands.process(image_rgb)
if results.multi_hand_landmarks:
        for landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, landmark, mp_hands.HAND_CONNECTIONS)

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()