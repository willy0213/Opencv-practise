import cv2

cap = cv2.VideoCapture('Yee.mp4')
# cap = cv2.VideoCapture(0) 會出現自己電腦鏡頭

while True:
    ret, frame = cap.read()  # read函數會回傳兩個值，第一個值為布林值(有沒有正確取得下一偵)=ret，第二個值就是有成功他會回傳取的到的下一張圖片=frame
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)  # 更改影片大小
        cv2.imshow('video', frame)
    else:
        break
    # cv2.waitKey(1)
    if cv2.waitKey(10) == ord('q'):    # 按鍵盤上的 q 影片會提前結束
        break
