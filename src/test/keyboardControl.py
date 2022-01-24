from djitellopy import tello
import keyPressModule as kpm
from time import sleep
# make the string in 'getKey' the selected key to use
kpm.init()
drone = tello.Tello()
drone.connect()

def getKeyBoardInput():
    # lr is left & right
    # fb is front & back
    # ud is up & down
    # yv is yaw & velocity
    lr, fb, ud,  yv = 0, 0, 0, 0
    speed = 50

    if kpm.getKey("LEFT"): lr  = -speed 
    elif kpm.getKey("RIGHT"): lr  = speed 

    if kpm.getKey("UP"): fb  = speed 
    elif kpm.getKey("DOWN"): fb  = -speed

    if kpm.getKey("w"): ud  = speed
    elif kpm.getKey("s"): ud  = -speed

    if kpm.getKey("a"): yv  = speed
    elif kpm.getKey("d"): yv  = -speed

    if kpm.getKey("q"): drone.land()
    if kpm.getKey("t"): drone.takeoff()
    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput() 
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)