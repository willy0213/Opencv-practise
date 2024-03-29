import cv2

img = cv2.imread('shape.jpg')
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)    # 檢測邊緣，第二參數最小值，第三為最大值
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 偵測圖片輪廓，第一個參數為要偵測的輪廓，第二個為模式(外輪廓、內輪廓等)，第三個參數為近似方法(水平壓縮等）
# 會回傳兩個值，contours 和 hierarchy

for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
# 畫出輪廓，第一個參數為畫在哪張圖片，第二個參數為要畫的輪廓，第三個參數為要畫的輪廓是第幾個(-1=全部)，第四個參數為輪廓的顏色，第五個參數為粗度

    print(cv2.contourArea(cnt))   # 印出面積

    print(cv2.arcLength(cnt, True))     # 印出周長，第二參數為是否閉合(True of False)

    peri = cv2.arcLength(cnt, True)
    vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
    print(vertices)

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)