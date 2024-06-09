import time

from serial.tools import list_ports
from ultralytics import YOLO
from threading import Lock, Thread
from serial import Serial
from time import sleep
import cvzone
import torch
import cv2


class ArduinoSerial:

    def __init__(self):
        ports = [str(port) for port in list_ports.comports()]
        # arduino_port = next(filter(lambda p: 'Arduino' in p, ports)).split(' ')[0].strip()
        arduino_port = ports[0].split(' ')[0].strip()

        self.serial_object = Serial(arduino_port)
        self.serial_object.baudrate = 9600

        sleep(3)

    def send_message(self, message):
        self.serial_object.write(f'{message}\n'.encode('utf-8'))
        sleep(0.1)


def map(x, a, b, c, d):
    y = (x - a) / (b - a) * (d - c) + c
    return y


# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture('rtsp://admin:Aa2610200@192.168.1.64/doc/page/preview.asp')
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

frame = None
lo = Lock()


def rtsp_cam_buffer():
    global frame, lo, last

    while True:

        with lo:
            _, frame = cap.read()


t = Thread(target=rtsp_cam_buffer)
t.daemon = True
t.start()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
drone_model = YOLO('yolov9d1.pt').to(device)

arduino_serial = ArduinoSerial()
previous_time = time.time()
while cap.isOpened():

    if frame is None:
        continue

    result = drone_model.predict(frame)
    for detection in result:
        boxes = sorted(detection.boxes, key=lambda b: b.xywh[0][2] * b.xywh[0][3])

        if boxes:
            box = boxes[-1]
            if box.conf[0].item() < 0.7:
                continue

            x, y, w, h = box.xywh[0]
            rect = int(x - w / 2), int(y - h / 2), int(w), int(h)

            distance = -(x - frame.shape[1] / 2)
            if abs(distance) > 200 and (time.time() - previous_time > 0.1):
                previous_time = time.time()
                arduino_serial.send_message(int(distance * 0.80))

            cvzone.cornerRect(frame, rect, l=5, rt=3)

    try:
        cv2.imshow('frame', frame)

    except cv2.error:
        cap.release()
        cap = cv2.VideoCapture('rtsp://admin:Aa2610200@192.168.1.64/doc/page/preview.asp')
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        continue

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()