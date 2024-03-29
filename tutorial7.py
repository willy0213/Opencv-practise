import cv2

img = cv2.imread('qq.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # 轉換成灰階圖片
faceCascade = cv2.CascadeClassifier('face_detect.xml')         # 載入模型
faceRect = faceCascade.detectMultiScale(gray, 1.1, 4)    # 偵測圖片，第一個參數為來源，第二個參數為縮小的倍數，第三個為辨識的嚴謹度
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 畫矩形(來源，長度，寬度，顏色，粗度)

cv2.imshow('img', img)
cv2.waitKey(0)