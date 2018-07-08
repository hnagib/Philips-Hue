import cv2
import numpy as np
from phue import Bridge

def get_hsv(hsv, x, y):
    return [int((hsv[y,x][0]/179)*65535), int(hsv[y,x][1]), int(hsv[y,x][2])]

def set_hsv(light, hsv_val):
    light.hue = hsv_val[0]
    light.saturation = hsv_val[1]
    light.brightness = 255

# Connect to Philips Hue
b = Bridge('192.168.2.44')
b.connect()
study_light = b.lights[2]

# Read frames from built-in camera
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    set_hsv(study_light, get_hsv(hsv, 100, 400))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()