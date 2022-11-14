import cv2 , numpy as np

#배경 배열 생성   
img = np.zeros(shape = (512 , 512 , 3), dtype = np.uint8) + 255 # +255 하면 전체 값에 255로 변경하여 흰 배경
# img = np.ones(( 512 , 512 , 3),np.uint8) * 255
# img = np.fill((512 , 512 ,3 ), (255 , 255 , 255), dtype = np.uint8)
# img = np.zeros((512 , 512 ,3),np.uint8)

#사각형
pt1 = 100 , 100 # pt1 최소 시작 점 
pt2 = 400 , 400 # pt2 최대 끝 점
#           배열 , 시작점, 끝점(  , 색 ,  ) , 두께 )
cv2.rectangle(img , pt1 ,pt2 , (0 ,255 ,0) ,2 )

#끝부분 선
#              (중심) , (좌표)   , (색상)     , 두께 )
cv2.line(img , (0,0) , (500, 0) , (255, 0, 0), 5)
cv2.line(img , (0,0) , (0, 500) , (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
