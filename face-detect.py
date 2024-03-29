import cv2

# 初始化攝影機
cap = cv2.VideoCapture(0)  # 0 表示第一個攝影機

# 載入人臉辨識模型
faceCascade = cv2.CascadeClassifier('face_detect.xml')

while True:
    # 從攝影機捕捉一幀視訊
    ret, frame = cap.read()

    # 將幀轉換成灰階圖片
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faceRect = faceCascade.detectMultiScale(gray, 1.07, 4)

    # 繪製矩形框
    for (x, y, w, h) in faceRect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 顯示視訊
    cv2.imshow('Face Detection', frame)

    # 按下 'q' 鍵退出迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機資源
cap.release()
cv2.destroyAllWindows()
