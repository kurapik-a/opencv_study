import cv2
import numpy as np

# 读取图像并转为灰度图
img = cv2.imread('cat.14.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. 简单阈值二值化
_, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 2. 反向二值化
_, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 3. 截断阈值
_, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

# 4. 阈值化为0
_, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)

# 5. 反向阈值化为0
_, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

# 6. 大津算法（自动阈值）
_, thresh6 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 7. 三角形算法（自动阈值）
_, thresh7 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

# 8. 自适应阈值 - 均值
thresh8 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 11, 2)

# 9. 自适应阈值 - 高斯
thresh9 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 11, 2)

print("所有二值化操作完成！")

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.imshow('video', thresh9)
cv2.waitKey(0)

cv2.destroyAllWindows()