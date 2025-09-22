import cv2

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
img = cv2.imread('cat.1.jpg')
cv2.imshow('img', img)



while True:
    key = cv2.waitKey(0)
    if (key & 0xFF) == ord('q'):
        break
    elif (key & 0xFF) == ord('s'):
        cv2.imwrite(r'./cat.png', img)
    else:
        print(chr(key))

cv2.destroyAllWindows()
