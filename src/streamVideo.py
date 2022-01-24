from djitellopy import tello
import cv2

# Code
drone = tello.Tello()
drone.connect()

drone.streamon()
def streamith():
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (500, 350))
        img = cv2.flip(img, 0)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
streamith()