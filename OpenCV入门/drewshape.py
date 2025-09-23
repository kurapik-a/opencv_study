import cv2
import numpy as np

# 全局变量
drawing = False  # 是否正在绘制
mode = 'line'    # 当前模式：'line'或'circle'
start_point = (-1, -1)  # 起始点
current_point = (-1, -1)  # 当前鼠标位置

# 创建黑色背景图像
img = np.zeros((500, 800, 3), dtype=np.uint8)

# 鼠标回调函数
def draw_shape(event, x, y, flags, param):
    global drawing, start_point, current_point, img
    
    current_point = (x, y)  # 更新当前鼠标位置
    
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        drawing = True
        start_point = (x, y)
        
    elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动
        if drawing:
            # 创建临时图像用于实时预览
            temp_img = img.copy()
            if mode == 'line':
                cv2.line(temp_img, start_point, (x, y), (0, 255, 0), 2)
            elif mode == 'circle':
                radius = int(np.sqrt((x - start_point[0])**2 + (y - start_point[1])**2))
                cv2.circle(temp_img, start_point, radius, (255, 0, 0), 2)
            cv2.imshow('Drawing Board', temp_img)
            
    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键释放
        drawing = False
        if mode == 'line':
            cv2.line(img, start_point, (x, y), (0, 255, 0), 2)
        elif mode == 'circle':
            radius = int(np.sqrt((x - start_point[0])**2 + (y - start_point[1])**2))
            cv2.circle(img, start_point, radius, (255, 0, 0), 2)
        cv2.imshow('Drawing Board', img)

# 创建窗口并设置鼠标回调
cv2.namedWindow('Drawing Board')
cv2.setMouseCallback('Drawing Board', draw_shape)

print("使用说明：")
print("按 'l' 键：切换到画线模式")
print("按 'c' 键：切换到画圆模式") 
print("按 'q' 键：退出程序")
print("当前模式：画线")

cv2.imshow('Drawing Board', img)

while True:
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('l'):  # 切换到画线模式
        mode = 'line'
        print("当前模式：画线")
        
    elif key == ord('c'):  # 切换到画圆模式
        mode = 'circle'
        print("当前模式：画圆")
    elif (key & 0xFF) == ord('s'):
        cv2.imwrite(r'./cat.png', img)
        
    elif key == ord('q'):  # 退出程序
        break

cv2.destroyAllWindows()