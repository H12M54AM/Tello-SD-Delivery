from djitellopy import tello
from getbattery import saucemeter

drone = tello.Tello()
drone.connect()

# code
def targetLock():
    drone.enable_mission_pads()
    drone.set_mission_pad_detection_direction(1)  # forward detection only  只识别前方

    drone.takeoff()

    pad = drone.get_mission_pad_id()

    # detect and react to pads until we see pad #1

    while pad != 1:
        if pad == 3:
            drone.rotate_clockwise(90)

        if pad == 4:
            drone.flip_forward()

        pad = drone.get_mission_pad_id()
        
    drone.disable_mission_pads()
    drone.land()
    drone.end()

saucemeter()