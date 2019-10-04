import RPi.GPIO as GPIO
import time

LedPin = 11
ButPin = 12

Led_status = 1

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.setup(ButPin, GPIO.IN)
	GPIO.output(LedPin, GPIO.HIGH)

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)
	if Led_status == 1:
		print("LED on")
	else:
		print("LED off")

def loop():
	GPIO.add_event_detect(ButPin, GPIO.FALLING, callback=swLed, bouncetime=20)
	while True:
		time.sleep(0.5)
def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
