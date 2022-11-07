# 0204.py

import cv2
from matplotlib import pyplot as plt

imageFile = '/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

plt.imshow(imgGray, cmap='gray', interpolation='bicubic')

plt.show()