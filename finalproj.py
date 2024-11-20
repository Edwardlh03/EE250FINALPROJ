from grovepi import *
import time
import math
dht_sensor_port = 7
ultrasonic_ranger = 4
light_sensor = 1
sound_sensor = 0
pinMode(light_sensor,"INPUT")
while True:
    try:
        [temp, hum] = dht(7,0)
        time.sleep(0.05)
        if math.isnan(temp) == False and math.isnan(hum) == False:
            print("temp =", temp, "C\thumidity =", hum,"%")
        # [temp, hum] = dht(dht_sensor_port,0)

        # print("temp =", temp, "C\thumidity =", hum,"%")
        # # Read distance value from Ultrasonic
        # dist = ultrasonicRead(4)
        # print(ultrasonicRead(0), ultrasonicRead(1), ultrasonicRead(2), ultrasonicRead(3), ultrasonicRead(4), ultrasonicRead(5), ultrasonicRead(6), ultrasonicRead(7))
        # print(dist,'cm')
        # # Get sensor value.  Read the light sensor.
        # light_value = analogRead(light_sensor)
        # sound_value = analogRead(sound_sensor)
        # print(light_value, 'light units,', sound_value, 'sound units')
        # time.sleep(1)
    except Error:
        pass