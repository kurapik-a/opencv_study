from os import close
import cv2
from matplotlib.ft2font import KERNING_UNSCALED
import numpy as np


def filter_bboxes_by_area(bboxes, min_area=1000):
    """
    根据边界框面积过滤掉过小的边界框
    
    参数:
        bboxes: 边界框列表，每个边界框格式为[x, y, w, h]
        min_area: 最小面积阈值，默认1000平方像素
        
    返回:
        filtered_bboxes: 过滤后的边界框列表
    """
    filtered_bboxes = []
    
    for bbox in bboxes:
        x, y, w, h = bbox
        area = w * h
        if area >= min_area:
            filtered_bboxes.append(bbox)
    
    return filtered_bboxes


cap = cv2.VideoCapture('video.mp4')

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

bgsubmog = cv2.createBackgroundSubtractorKNN()
while True:
    ret, frame = cap.read()
    
    if ret == True:
        #灰底
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #去燥
        blur = cv2.GaussianBlur(frame,(5,5),5)
        

        mask = bgsubmog.apply(blur)
        erode = cv2.erode(mask,kernal)
        dilate = cv2.dilate(erode,kernal,iterations=3)
        # erode = cv2.erode(dilate,kernal)

        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernal)
        close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernal)

        cnts, h = cv2.findContours(close, cv2.MORPH_CLOSE,cv2.CHAIN_APPROX_SIMPLE)


        for i,c in enumerate(cnts):
            area = cv2.contourArea(c)
            if area > 700:
                x, y, w, h = cv2.boundingRect(c)
                aspect_ratio = w / h
                if 0.2 < aspect_ratio < 5.0:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(frame, f"{int(area)}", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                

        cv2.imshow('video', frame)

    key = cv2.waitKey(40) & 0xFF

    if key == 27:
        break
    elif key == ord('s'):
        cv2.imwrite(r'./car.png', frame)


cap.release()
cv2.destroyAllWindows()
