import cv2
import numpy as np
'''(y,x)'''
img = np.zeros((480,640,3),np.uint8)

#split的使用
# b,g,r = cv2.split(img)

# b[10:100, 10:100] = 255

# cv2.imshow('img', img)
# cv2,cv2.imshow('b', b)
# cv2.waitKey(0)
'''画线x，y'''
cv2.line(img,(10,20), (300,400), (0,0,255),5,4)
#elipse()画椭圆
#po;ylines()画多变形
#fillPoy（）多变形填充
#putTrxt()数字填充
cv2.imshow('draw',img)
cv2.waitKey(0)