from djitellopy import tello
import cv2

# Code
drone = tello.Tello()
drone.connect()

def streamith():
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (500, 350))
        cv2.imshow("Image", img)
        cv2.waitKey(1)
streamith()