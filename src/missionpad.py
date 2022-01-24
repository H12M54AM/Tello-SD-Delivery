from djitellopy import tello

drone = tello.Tello()
drone.connect()

# code
def targetLock():
    drone.enable_mission_pads()

    drone.takeoff()

    pad = drone.get_mission_pad_id()
    detection = drone.set_mission_pad_detection_direction(1)
    # detect and react to pads until we see pad #1

    # Route
    drone.move_up(50)

        

    while pad != 1:
        if pad == 3:
            drone.rotate_clockwise(90)

        if pad == 4:
            drone.land()

        pad = drone.get_mission_pad_id()
        
    drone.disable_mission_pads()
    drone.land()
    drone.end()
targetLock()