import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

while True:
	try:
		GPIO.output(11, GPIO.HIGH)
		print("LED ON")
		time.sleep(1)
		GPIO.output(11, GPIO.LOW)
		print("LED OFF")
		time.sleep(1)
	except KeyboardInterrupt :
		GPIO.output(11, GPIO.LOW)
		exit()
