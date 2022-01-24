from djitellopy import tello
from getbattery import saucemeter
from missionpad import targetLock
from streamVideo import streamith
import theWatcher

# Connection
drone = tello.Tello()
drone.connect()

# Code

saucemeter()
theWatcher()
targetLock()
