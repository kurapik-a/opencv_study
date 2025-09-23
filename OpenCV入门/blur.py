import cv2
import numpy as np

# 读取图像
img = cv2.imread('dog.293.jpg')

# 1. 均值滤波
blur = cv2.blur(img, (5, 5))  # 核大小(5,5)

# 2. 高斯滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 0)  # 核大小, 标准差(0表示自动计算)

# 3. 中值滤波
median = cv2.medianBlur(img, 5)  # 核大小(必须是奇数)

# 4. 双边滤波
bilateral = cv2.bilateralFilter(img, 9, 75, 75)  # 直径, 颜色sigma, 空间sigma

# 5. 自定义滤波
kernel = np.ones((5, 5), np.float32) / 25  # 创建5x5均值核
custom = cv2.filter2D(img, -1, kernel)  # -1:输出深度与输入相同

# 6. 方框滤波
box = cv2.boxFilter(img, -1, (5, 5))  # 类似均值滤波但可控制归一化

# 7. 形态学滤波 - 腐蚀
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
erosion = cv2.erode(img, kernel, iterations=1)

# 8. 形态学滤波 - 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)

# 9. 形态学滤波 - 开运算
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 10. 形态学滤波 - 闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 11. 导向滤波 (需要OpenCV contrib模块)
# guided = cv2.ximgproc.guidedFilter(guide, img, radius, eps)

# 12. 非局部均值去噪
denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Sobel滤波 - 边缘检测
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # x方向梯度
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # y方向梯度
# sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # 合并梯度
# sobel_combined = sobel_x+sobel_y
sobel_combined = cv2.add(sobel_x,sobel_y)


# 2. Scharr滤波 - 更精确的Sobel
scharr_x = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(gray, cv2.CV_64F, 0, 1)

# 3. Laplacian滤波 - 二阶导数边缘检测
laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)

# 4. Canny边缘检测
canny = cv2.Canny(gray, 150, 200)  # 阈值1, 阈值2


'''高通滤波检测边沿用'''
print("所有滤波操作完成！")

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.imshow('video', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
