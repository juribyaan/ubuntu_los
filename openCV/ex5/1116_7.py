import cv2 ,numpy as np 
from matplotlib import pyplot as plt

src= np.array( [[0,0,0,0],
                [1,1,3,5],
                [6,1,1,6],
                [4,3,1,7]], dtype = np.uint8)

hist = cv2.calcHist(images = [src],channels = [0],mask=None,histSize=[4] ,ranges = [0,8])
print(hist)#범위

backP=cv2.calcBackProject([src],[0],hist,[0,8],scale=1)
print( backP)
