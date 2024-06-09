import torch
import cv2
import cvzone
from ultralytics import YOLO

# Load the drone detection model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
drone_model = YOLO('yolov9d1.pt').to(device)

# Load the image
image = cv2.imread('test14.jpg')

# Perform object detection
result = drone_model.predict(image)

# Process the detection results
for detection in result:
    boxes = sorted(detection.boxes, key=lambda b: b.xywh[0][2] * b.xywh[0][3])

    if boxes:
        box = boxes[-1]
        if box.conf[0].item() < 0.7:
            continue

        x, y, w, h = box.xywh[0]
        rect = int(x - w / 2), int(y - h / 2), int(w), int(h)

        # Calculate the distance (you may need to adjust this calculation based on your specific use case)
        distance = -(x - image.shape[1] / 2)

        # Print the distance (replace this with your desired action)
        print(f'Distance: {distance}')

        # Draw a rectangle around the detected drone
        cvzone.cornerRect(image, rect, l=5, rt=3)

# Display the image with the detected drone
cv2.imshow('frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()