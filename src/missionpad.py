from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
height = drone.get_height()

# code
def targetLock():
    drone.enable_mission_pads()
    pad = drone.get_mission_pad_id()
    detection = drone.set_mission_pad_detection_direction(2)

    # Route-----------------------------------------------------

    # This route is made for testing and is not the true route
    drone.takeoff()
    # 50cm
    drone.move_up(60) # in cm
    # 330cm
    drone.send_rc_control(10, 0, 0, 0)
    drone.move_forward(150)
    drone.move_back(20)

    def stepTwo():
        # To move back and counter the momentum
        drone.send_rc_control(0, -20, 0, 0)
        # Turn Left
        drone.send_rc_control(0, 0, 0, -50)
        sleep(1.5)
        # Counter
        drone.send_rc_control(0, 0, 0, 5)

        # Move Forward
        drone.send_rc_control(-50, 0, 0, 0)
     
    while pad != 1:
        if pad == 3:
            stepTwo()
            
        elif pad == 4:
            # Counter Forward
            drone.send_rc_control(10, 0, 0, 0)
            # To move back and counter the momentum
            drone.send_rc_control(0, -30, 0, 0)
            drone.move_down(20)
            drone.disable_mission_pads()
            drone.land()

    pad = drone.get_mission_pad_id()
    
    drone.disable_mission_pads()
    drone.land()
    drone.end()

targetLock()