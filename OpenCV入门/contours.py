import cv2
import numpy as np
from torch import binary_cross_entropy_with_logits

img = cv2.imread('dog.293.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours,-1,(0, 0 ,255), 1)
# cv2.imshow('img', binary)ss
cv2.imshow('img', img)
cv2.waitKey(0)
