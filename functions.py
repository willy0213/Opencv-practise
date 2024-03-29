import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)    # 3*3陣列
kernel1 = np.ones((3, 3), np.uint8)

img=cv2.imread('colercoler.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉換成灰階
blur = cv2.GaussianBlur(img, (15, 15), 10)     # 將圖片變模糊，其中第二個參數為值，第三個為標準差，第二個參數只能為奇數
canny = cv2.Canny(img, 100, 150)               # 取邊緣，第二個參數為最小門檻值，第三個為最大門檻值
dilate = cv2.dilate(canny, kernel, iterations=1)   # 膨脹圖片，第二個參數為和(為一個陣列)，第三個為次數
erode = cv2.erode(dilate, kernel1, iterations=2)   # 侵蝕圖片，第二個參數為和(為一個陣列)，第三個為次數

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)

cv2.waitKey(0)
