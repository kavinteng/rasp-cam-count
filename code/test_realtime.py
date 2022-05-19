import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
model.conf = 0.5
model.iou = 0.4

size_img_vdo = (640, 360)
color = (0, 0, 255)
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame, size_img_vdo)
    # results = model(frame, size=640)
    # out2 = results.pandas().xyxy[0]
    # if len(out2) != 0:
    #     for i in range(len(out2)):
    #         output_landmark = []
    #         xmin = int(out2.iat[i, 0])
    #         ymin = int(out2.iat[i, 1])
    #         xmax = int(out2.iat[i, 2])
    #         ymax = int(out2.iat[i, 3])
    #         obj_name = out2.iat[i, 6]
    #         if obj_name == 'person' or obj_name == '0':
    #             cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()