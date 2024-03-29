import cv2
import numpy as np
import random

img = cv2.imread('colercoler.jpg')

# print(type(img))   # 印出資料型態   #ndarray，nd=多維，array=陣列
# print(img.shape)   # 維度大小   [長,寬,顏色數量]

# img = np.empty((300, 300, 3), np.uint8)   # 設定寬高為300,BGR為3,8位元的無號整數

# for row in range(300):
#    for col in range(300):
#    for col in range(img.shape[1]):
#        img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]  # 指定隨機顏色 使用random
#        img[row][col] = [45, 78, 160]   # 固定數字的 B G R

# newimg = img[:150, :200]  # 切出圖片
newimg = img[400:650, 100:400]  # 切出圖片，兩個數字為範圍

cv2.imshow('img', img)
cv2.imshow('newing', newimg)
cv2.waitKey(0)
