import cv2

cv2.namedWindow('video', cv2.WINDOW_NORMAL)


# cap = cv2.VideoCapture(0)  #从摄象头读取
cap = cv2.VideoCapture(r'103236.mp4')#从视频文件读取

while True:
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    key = cv2.waitKey(40)

    if key != -1:
        if (key & 0xFF) == ord('q'):
            break
        elif (key & 0xFF) == ord('s'):
            cv2.imwrite(r'./cat.png', frame)
        else:
            print(chr(key))
            pass

cap.release()
cv2.destroyAllWindows()