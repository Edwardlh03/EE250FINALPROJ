dht_sensor_port = 7

while True:
	try:
		[ temp,hum ] = dht(dht_sensor_port,1)		#Get the temperature and Humidity from the DHT sensor
		print("temp =", temp, "C\thumidity =", hum,"%") 	
		t = str(temp)
		h = str(hum)

ultrasonic_ranger = 4

while True:
    try:
        # Read distance value from Ultrasonic
        distant = ultrasonicRead(ultrasonic_ranger)
        print(distant,'cm')

light_sensor = 0										# Connect the light sensor to A0 Port.
grovepi.pinMode(light_sensor,"INPUT")	
while True:
    try:
        # Get sensor value.  Read the light sensor.
        sensor_value = grovepi.analogRead(light_sensor)
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300
sensor_value = grovepi.analogRead(potentiometer)

        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

        # Calculate rotation in degrees (0 to 300)
        degrees = round((voltage * full_angle) / grove_vcc, 2)
