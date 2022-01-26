from djitellopy import tello

# connection
drone = tello.Tello()
drone.connect()

# Code
battery = drone.get_battery()

def saucemeter():
    while battery == battery:
        print(" ")
        print(f'Power is at: {battery}%')
        print(" ")
        if battery == 20:
            print(" ")
            print("Power is at: Low Battery")
            print(" ")
        if battery == 100:
            print(" ")
            print("Power is: Ready to rock and roll :)")
            print(" ")
        if battery < 10:
            print(" ")
            print("Power is: Very Low")
            print(" ")
        break
saucemeter()