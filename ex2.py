import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lena.png',0)
img[0:,0:36] = 0
img[0:36,0:] = 0
img[220:,0:] = 0
img[0:,220:] = 0
cv2.imshow('image',img)
cv2.waitKey(0)