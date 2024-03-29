import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('beat.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.namedWindow('TrackBar')                     # 創建一個視窗
cv2.resizeWindow('TrackBar', 640, 320)          # 第二參數為視窗寬度，第三參數為視窗高度

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)
# 創建TrackBar，第一參數為名稱，第二為參數為來源，第三為初始值，第四為最高值，第五為拉動後要執行的函數

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      # 將圖片轉換成HSV

while True:
    h_min = cv2.getTrackbarPos('Hue Min', "TrackBar")     # 得到TrackBar數值，第一參數為來源，第二為視窗名稱
    h_max = cv2.getTrackbarPos('Hue Max', "TrackBar")
    s_min = cv2.getTrackbarPos('Sat Min', "TrackBar")
    s_max = cv2.getTrackbarPos('Sat Max', "TrackBar")
    v_min = cv2.getTrackbarPos('Val Min', "TrackBar")
    v_max = cv2.getTrackbarPos('Val Max', "TrackBar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)     # 過濾圖片，第一參數來源，第二參數最小值，第三參數最大值
    result = cv2.bitwise_and(img, img, mask=mask)     # 可以展顯出被過濾後與原圖的差別
    cv2.waitKey(1)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
