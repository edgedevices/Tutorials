import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MCP3208

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

adc0 = MCP3208(channel = 0)

while True:
	if adc0.value > 0.3: #watering threshold
		moisture = adc0.value
		print(moisture)
		print('watering')
		GPIO.output(13, True) #turn pump on
		sleep(2) #water length
		GPIO.output(13, False) #turn pump off
		print('watered')
		sleep(2)
	else:
		print('watered')
		sleep(2)
		moisture = adc0.value
		print(moisture)
