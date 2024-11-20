from grovepi import *
import time
dht_sensor_port = 7
ultrasonic_ranger = 4
light_sensor = 1
sound_sensor = 0
pinMode(light_sensor,"INPUT")
while True:
    try:
        [temp, hum] = dht(dht_sensor_port,1)
        print("temp =", temp, "C\thumidity =", hum,"%")
        # Read distance value from Ultrasonic
        dist = ultrasonicRead(ultrasonic_ranger)
        print(dist,'cm')
        # Get sensor value.  Read the light sensor.
        light_value = analogRead(light_sensor)
        sound_value = analogRead(sound_sensor)
        print(light_value, 'light units,', sound_value, 'sound units')
        time.sleep(1)
    except Error:
        pass