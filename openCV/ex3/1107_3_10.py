import cv2 , numpy as np



img=np.zeros(shape=(512,512,3),dtype=np.uint8)+255


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()