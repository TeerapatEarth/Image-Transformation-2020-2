import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lena.png',0)
img[125:141,120:192] = 0
cv2.imshow('image',img)
cv2.waitKey(0)
