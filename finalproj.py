from grovepi import *
import time
import math
import paho.mqtt.client as mqtt

dht_sensor_port = 7
ultrasonic_ranger = 4
potentiometer = 2
light_sensor = 1
sound_sensor = 0
pinMode(light_sensor,"INPUT")
pinMode(potentiometer, "INPUT")
pinMode(sound_sensor, "INPUT")

grove_vcc = 5
adc_ref = 5

full_angle = 300

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    
#Default message callback. Please use custom callbacks.
def custom_message(client, userdata, message):
    if str(message.payload, "utf-8") == "Button pressed!":
        print("Button pressed!")
    else:
        print("VM: " + str(message.payload, "utf-8") + " cm")

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = custom_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()
    
    while True:
        try:
            [temp, hum] = dht(7,0)
            if math.isnan(temp) == False and math.isnan(hum) == False:
                print("temp =", temp, "C\thumidity =", hum,"%")
            # [temp, hum] = dht(dht_sensor_port,0)
    
            # print("temp =", temp, "C\thumidity =", hum,"%")
            # # Read distance value from Ultrasonic
            _, _, _, _, dist, _, _, _ = ultrasonicRead(0), ultrasonicRead(1), ultrasonicRead(2), ultrasonicRead(3), ultrasonicRead(4), ultrasonicRead(5), ultrasonicRead(6), ultrasonicRead(7)
            if dist != 65535:
                print(dist)
            if dist < 50:
                client.publish("jackmitc/ultrasonicranger", "1")
            
            # print(ultrasonicRead(0), ultrasonicRead(1), ultrasonicRead(2), ultrasonicRead(3), ultrasonicRead(4), ultrasonicRead(5), ultrasonicRead(6), ultrasonicRead(7))
            # print(dist,'cm')
            # # Get sensor value.  Read the light sensor.
            light_value = analogRead(light_sensor)
            sound_value = analogRead(sound_sensor)
            if light_value < 50:
                client.publish("jackmitc/lightsensor", "1")
            if sound_value < 50:
                client.publish("jackmitc/soundsensor", "1")
            print(light_value, 'light units,', sound_value, 'sound units')
    
            # time.sleep(1)
            potentval = analogRead(potentiometer)
            if(potentval != 65535):
                print(potentval)
            if potentval < 50:
                client.publish("jackmitc/rotaryencoder", "1")
            
            # print(potentiometer)
            # print(analogRead(potentiometer))
            # sensor_value = analogRead(potentiometer)
            # voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
            # degrees = round((voltage * full_angle) / grove_vcc, 2)
            # print(voltage, degrees)
            # print(round((float)(analogRead(potentiometer)) * adc_ref / 1023, 2), round((round((float)(analogRead(potentiometer)) * adc_ref / 1023, 2) * full_angle) / grove_vcc, 2))
            # time.sleep(1)
    
        except Error:
            pass
