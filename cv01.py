import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    cv2.imshow('WebCam', img)
    
    # Тут вставляем код обработки каждого кадра

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()