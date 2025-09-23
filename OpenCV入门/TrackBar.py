import cv2
import numpy as np

def callback():
    pass 

cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

cv2.createTrackbar('R', 'trackbar', 0,255,callback)
cv2.createTrackbar('G', 'trackbar', 0,255,callback)
cv2.createTrackbar('B', 'trackbar', 0,255,callback)

img = np.zeros((640,480,3), np.uint8)

while True:
    cv2.imshow('trackbar',img)
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    img[:] = [b,g,r]
    key = cv2.waitKey(10)
    if key != -1:
        if (key & 0xFF) == ord('q'):
            break
        elif (key & 0xFF) == ord('s'):
            cv2.imwrite(r'./cat.png', img)
        else:
            print(chr(key))
            pass

cv2.destroyAllWindows()