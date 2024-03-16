from gpiozero import DistanceSensor
from signal import pause

sensor = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.2)

while True:
    if sensor.distance <=0.4:
        print("WARNING! GET AWAY!")
    else:
        print("Hi, Welcome!")
