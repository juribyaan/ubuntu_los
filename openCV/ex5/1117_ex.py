#0505.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

imageFile = 'C:/Users/505/ubuntu_los/openCV/data/infrared_road.jpg'
img = cv2.imread(imageFile)

imgRGB1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
(H, W) = imgRGB1.shape[:2]
# h = imgRGB1.shape[0]
# w = imgRGB1.shape[0]
# fig, ax = plt.subplots(2,2, figsize = (10,10), sharey = True)
# fig.canvas.manager.set_window_title("head")
h_num = 5
w_num = 7
imgRGB1_array_len = len(imgRGB1[0])
imgRGB1_len = len(imgRGB1)
# cv2.line(img=imgRGB1, #그릴 그림
#          pt1= (100,100) , pt2= (250 , 500), #튜플
#         #  color= (255,255,255) ,
#         color= (0,0,255) ,
#          thickness= 1, #정수만
#          lineType= cv2.LINE_4, #cv2.LINE_8, cv2.LINE_AA,
#         )
#         #  shift=100 )#그리기 좌표값의 축소 비율)
# cv2.line(imgRGB1, (50, 50), (150, 150),(255,255,255))
# cv2.line(img, (50, 60), (150, 160),(0,255,255))
# cv2.line(img, (50, 70), (150, 170),(255,0,255))
# cv2.line(img, (50, 80), (150, 180),(255,255,0))
#

# cv2.line(img, (0, 50), (W, 50),(0,0,0)) # 수평선
# cv2.line(img, (50, 0), (50, H),(0,0,0)) # 수직선
# cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0))
# hsv = cv2.cvtColor(img[9:10,9:11], cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
# h = max(h)
# h
# v = max(max(v))
# v = str(v)
# v
h = H//h_num
w = W//w_num
# cv2.putText(img, v, (w*3, h*4), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
for n in range(w_num+1):
    for m in range(h_num+1):
        cv2.line(img, ( 0 , h*m ) , ( W , h*m ) ,(255,255,255)  )
        cv2.line(img, ( w*n , 0 ) , ( w*n , H ) ,(255,255,255)  )
        #선의 중간 좌표
        # cv2.line(img, ( 0 , h*m-(h//2) ) , ( W , h*m-(h//2) ) ,(255,255,255)  )
        # cv2.line(img, ( w*n-(w//2) ,0 ) , ( w*n-(w//2) , H ) ,(255,255,255)  )
        # cv2.line(imgRGB1, ( w_num*n , h_num*m ) , ( w_num*n , h_num*m ) ,(255,255,255)  )
        hsv = cv2.cvtColor(img[w*n-(w//2):h*m-(h//2)], cv2.COLOR_BGR2HSV)
        z,x,v = cv2.split(hsv)
        # while True:
        #         try:
        #                 v = max(v)
        #         except ValueError and TypeError:
        #                 break

        v = str(v)
        
        cv2.putText(img, v, (w*n, h*m), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
        # cv2.putText(img, v, (9,10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))




# histColor = ('b', 'g', 'r')
# for i in range(3):
#     hist = cv2.calcHist(images=[img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
#     plt.plot(hist, color = histColor[i])    
# ax[0][0].axis('off')
# ax[0][0].imshow(imgRGB1, aspect='auto')
# ax[0][1].axis('off')
# ax[0][1].imshow(imgRGB1, aspect='auto')
# ax[1][0].axis('off')
# ax[1][0].imshow(plt.show(), aspect='auto')
# ax[1][1].axis('off')
# ax[1][1].imshow( aspect='auto')
# plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.05, hspace=0.05)

cv2.imshow('1',img)
# cv2.imshow('2',imgRGB1)
cv2.waitKey()
cv2.destroyAllWindows()

# plt.show()
