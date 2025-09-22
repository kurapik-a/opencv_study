import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

'''创建窗口'''
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

cap = cv2.VideoCapture(0)  #从摄象头读取
# cap = cv2.VideoCapture(r'103236.mp4')#从视频文件读取

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

Vm = cv2.VideoWriter('./out.avi',fourcc,24,(frame_width,frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    cv2.resizeWindow('video',640,480)

    key = cv2.waitKey(1)
    if ret == True:
        Vm.write(frame)
        if key != -1:
            if (key & 0xFF) == ord('q'):
                break
            elif (key & 0xFF) == ord('s'):
                cv2.imwrite(r'./cat.png', frame)
            else:
                print(chr(key))
                pass
    else:
        break

cap.release()
Vm.release()
cv2.destroyAllWindows()