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
