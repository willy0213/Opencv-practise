import cv2

img = cv2.imread('colercoler.jpg')  # 去讀這個照片

# img = cv2.resize(img, (300, 300)) 更改像素

img = cv2.resize(img, (0, 0), fx=2, fy=2)  # fx=2(寬度增加為兩倍)，fy=2(高度增加為兩倍)

cv2.imshow('img', img)  # show出這張照片，參數1為圖片名稱，參數2為圖片來源

cv2.waitKey(1000)  # 等待1秒，等待無限久為0
