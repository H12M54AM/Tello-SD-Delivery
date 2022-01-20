from djitellopy import tello
from getbattery import saucemeter

# Connection
drone = tello.Tello()
drone.connect()

# Code
drone.takeoff()
drone.rotate_clockwise(90)
saucemeter()
drone.land()