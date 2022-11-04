# 0203.py
import cv2
# from matplotlib import pyplot as plt 
import matplotlib.pyplot as plt
# import matplotlib
# import matplotlib matplotlib.use('TkAgg') 
# import matplotlib.pyplot as plt

imageFile = '/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/lena.jpg'
imgBGR = cv2.imread(imageFile)

#차트 축
plt.axis('off')

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
# plt.imshow(imgBGR)

plt.show()
