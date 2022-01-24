from djitellopy import tello

drone = tello.Tello()
drone.connect()

drone.takeoff()
drone.move_forward(125)
print(drone.get_height())
drone.land()