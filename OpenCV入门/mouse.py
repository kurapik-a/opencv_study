import cv2
import numpy as np

def mousr_callback(event, x, y, flags, userdata):
    print(event,x,y,flags,userdata)
    pass

#创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)
#设置鼠标回调
cv2.setMouseCallback('video', mousr_callback,123)
#显示窗口和背景
img = np.zeros((640,480),np.uint8)

while True:
    cv2.imshow('video', img)
    key = cv2.waitKey(1)

    if key != -1:
        if (key & 0xFF) == ord('q'):
            break
        elif (key & 0xFF) == ord('s'):
            cv2.imwrite(r'./cat.png', img)
        else:
            print(chr(key))
            pass

cv2.destroyAllWindows()