import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_PINS = [11, 13, 15, 29, 31, 18, 16, 12, 10, 8]

for pin in LED_PINS:
  GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
