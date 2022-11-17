#0505.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

src = cv2.imread('./data/lena.jpg')

histColor = ('b', 'g', 'r')

for i in range(3):
    hist = cv2.calcHist(images=[src], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color = histColor[i])

plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows()
