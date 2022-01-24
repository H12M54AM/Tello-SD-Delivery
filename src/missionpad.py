from djitellopy import tello

drone = tello.Tello()
drone.connect()
height = drone.get_height()

# code
def targetLock():
    drone.enable_mission_pads()
    pad = drone.get_mission_pad_id()
    detection = drone.set_mission_pad_detection_direction(2)

    # Route
    drone.takeoff()
    drone.move_up(100) # in cm
    drone.move_forward(330)
    print(f'The height is {height}cm high')
 
    while pad != 1:
        if pad == 3:
            drone.rotate_counter_clockwise(90)
            drone.move_forward(100)

        if pad == 4:
            drone.move_down(20)
            drone.land()

        pad = drone.get_mission_pad_id()
        
    drone.disable_mission_pads()
    drone.land()
    print(f'The drone has landed and the height was {height}cm high')
    drone.end()

targetLock()