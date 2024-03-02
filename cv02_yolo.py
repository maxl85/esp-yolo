import cv2
import requests
from ultralytics import YOLO

capture = cv2.VideoCapture(0)

model = YOLO("yolov8n.pt")

while True:
    ret, img = capture.read()
    
    # Ищем на кадре человека (classes=0)
    results = model.predict(source=img, classes=0, conf=0.8,  verbose=False)
    
    plot_res = results[0].plot(labels=True)
    
    # print("Total = ", results[0].boxes.shape[0])
    
    # Отправка запроса на esp32 на включении светодиода, если в кадре есть человек
    # if (results[0].boxes.shape[0] > 0):
    #     res = requests.get('http://192.168.1.1/ledon')
    #     print(res)
    # else:
    #     res = requests.get('http://192.168.1.1/ledoff')
    
    
    cv2.imshow('WebCam', plot_res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

