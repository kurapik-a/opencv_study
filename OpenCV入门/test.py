import cv2 as cv

# 1. 读取摄像头
cap = cv.VideoCapture(0)

# 2. 获取图像的属性（宽和高，）,并将其转换为整数
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 3. 创建保存视频的对象，设置编码格式，帧率，图像的宽高等
out = cv.VideoWriter('outpy.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))  # 保存视频
while(True):

    # 4.获取视频中的每一帧图像
    ret, frame = cap.read()
    if ret == True:

        # 5.将每一帧图像写入到输出文件中
        out.write(frame)  #视频写入
    else:
        break

# 6.释放资源
cap.release()
out.release()  #资源释放
cv.destroyAllWindows()