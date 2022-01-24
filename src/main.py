from djitellopy import tello
from getbattery import saucemeter
from missionpad import targetLock

# Connection
drone = tello.Tello()
drone.connect()

# Code

targetLock()
saucemeter()