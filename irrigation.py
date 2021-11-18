import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MCP3208

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) #Digital Output #1
GPIO.setup(20, GPIO.OUT) #Digital Output #2
GPIO.setup(21, GPIO.OUT) #Digital Output #3
GPIO.setup(26, GPIO.OUT) #Digital Output #4
GPIO.setup(19, GPIO.OUT) #Digital Output #5
GPIO.setup(13, GPIO.OUT) #Digital Output #6

adc0 = MCP3208(channel = 0) #Analog input #0

def main():
	try:
		while True:
			if adc0.value > 0.3: #watering threshold
				moisture = adc0.value
				print(moisture)
				print('watering')
				GPIO.output(16, True) #turn pump on
				sleep(2) #water length
				GPIO.output(16, False) #turn pump off
				print('watered')
				sleep(2)
			else:
				print('soil saturated')
				sleep(2)
				moisture = adc0.value
				print(moisture)

	except KeyboardInterrupt: # If CTRL+C, exit cleanly:
		GPIO.cleanup() # cleanup GPIOs
		
if __name__ == "__main__":
    main()
