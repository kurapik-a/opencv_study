import cv2
import numpy as np

curshape = 'line'
img = np.zeros((480, 640, 3), dtype=np.uint8)

def mousr_callback(event, x, y, flags, userdata):
    print(event,x,y,flags,userdata)


    pass

cv2.namedWindow('drew',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('drew', mousr_callback,'123')



while True:
    cv2.imshow('drew', img)
    key = cv2.waitKey(10) & 0xFF

    if key != 255:
        if (key) == ord('q'):
            print('退出')
            break
        elif (key) == ord('s'):
            cv2.imwrite(r'./cat.png', img)
            print('保存成功')
        elif (key) == ord('l'):
            curshape = 'line'
            print('画线模式')
        elif (key) == ord('c'):
            curshape = 'circel'
            print('画圆模式')
        else:
            print(chr(key))
            pass

cv2.destroyAllWindows()