import cv2 , numpy as np

#배경 배열 생성   
img = np.zeros(shape = (512 , 512 , 3), dtype = np.uint8) + 255 # +255 하면 전체 값에 255로 변경하여 흰 배경
# img = np.ones(( 512 , 512 , 3),np.uint8) * 255
# img = np.fill((512 , 512 ,3 ), (255 , 255 , 255), dtype = np.uint8)
# img = np.zeros((512 , 512 ,3),np.uint8)

#사각형
x1 , x2 = 100 , 400   
y1 , y2 = 100 , 400  
#           배열 , 시작점, 끝점(  , 색 ,  ) , 두께 )
cv2.rectangle(img , (x1, y1) , ( x2, y2 ), (0 ,255 ,0) )

pt1 = 120, 50
pt2 = 300, 500
cv2.line(img , pt1 ,pt2 ,( 255, 0 , 0) , 2)
imgRect = (x1,y1,x2-x1,y2-y1)
retval, rpt1, rpt2 = cv2.clipLine(imgRect,pt1,pt2)
if retval:
    cv2.circle(img,rpt1,radius = 5 , color = (0,255,0),thickness = -1)
    cv2.circle(img,rpt2,radius = 5 , color = (0,255,0),thickness = -1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
