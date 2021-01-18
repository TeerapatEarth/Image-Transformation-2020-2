import cv2
import matplotlib.pyplot as plt
img = cv2.imread('clena.png')
imRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(imRGB)
plt.show()
cv2.waitKey(0)