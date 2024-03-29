import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

cv2.line(img, (0, 0), (400, 300), (0, 255, 0), 2)  # 第一參數為目標，第二為直線起點位置，第三為終點，第四為顏色，第五為粗度
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)  # img.shape[1] = 圖片寬度，img.shape[0] = 圖片長度

cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), 2)       # 第一參數為目標，第二為左上，第三為右下，第四為顏色，第五為粗度
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED)    # cv2.FILLED = 填滿顏色

cv2.circle(img, (300, 400), 30, (255, 0, 0), 1)              # 第一參數為目標，第二為圓心座標，第三為半徑，第四為顏色，第五為粗度
cv2.circle(img, (300, 400), 30, (255, 0, 0), cv2.FILLED)           # cv2.FILLED = 填滿顏色

cv2.putText(img, 'Hello', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
# 第一參數為目標，第二為貼上去的字，第三為字左下角的位置，第四為字體，第五為字大小，第六為顏色，第七為字粗度
# 不支援寫中文

cv2.imshow('img', img)
cv2.waitKey(0)