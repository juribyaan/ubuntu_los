# 0202.py
import cv2

imageFile = '/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/lena.jpg'
img = cv2.imread(imageFile)

cv2.imwrite('/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/Lena.bmp', img)
cv2.imwrite('/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/Lena.png', img)
                                                                       #list로 전달 [첫번째 상수 , 압축률]
cv2.imwrite('/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9]) 
cv2.imwrite('/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 30])

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('/home/juribyaab/catkin_ws/src/ubuntu_los/openCV/data/lena.jpg',imgGray)