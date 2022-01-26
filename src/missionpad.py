from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
height = drone.get_height()
drone.set_speed(40)
# code

drone.enable_mission_pads()
pad = drone.get_mission_pad_id()

drone.takeoff()
# 50cm
drone.move_up(50) # in cm
# 230cm
drone.move_forward(180)

def targetLock():

    # Route-----------------------------------------------------

    # This route is made for testing and is not the true route

    if pad == 3:
        # To move back and counter the momentum
        sleep(0.5)
        drone.move_back(60)

    sleep(1)
    # Turn Left
    drone.rotate_counter_clockwise(90)
    sleep(1)

    # Move Forward
    drone.move_forward(450)
    
    if pad == 4:
        # To move back and counter the momentum
        drone.send_rc_control(0, -30, 0, 0)
        drone.land()
        drone.disable_mission_pads()
    else:
        drone.move_up(40)
        drone.rotate_clockwise(360)
        if pad == 4:
            sleep(1.5)
            drone.move_forward(25)
            drone.land()
            drone.disable_mission_pads()

targetLock()

drone.land()
drone.disable_mission_pads()