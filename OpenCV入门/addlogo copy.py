from os import TMP_MAX
import cv2
import numpy as np
from scipy.fft import dst

cat = cv2.imread('cat.14.jpg')

cv2.namedWindow('logo', cv2.WINDOW_NORMAL)
#创建logo
logo = np.zeros((20,20,3),np.uint8)
mask = np.zeros((20,20),np.uint8)

logo[5:15, 5:15] = [0,0,255]
logo[10:25, 10:20] = [0,255,0]

mask[5:15, 5:15] = 255
mask[10:20, 10:20] = 255
#对mask按位求反
m = cv2.bitwise_not(mask)

# 取出原图的添加位置（要求大小相同）
roi = cat[100:120,100:120]
tmp = cv2.bitwise_and(roi, roi, mask=m)
dst = cv2.add(tmp,logo)
cat[100:120,100:120] = dst
cv2.imshow('logo',cat)
cv2.waitKey(0)