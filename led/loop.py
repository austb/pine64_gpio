import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SLEEP_TIME=0.2
LED_PINS = [11, 13, 15, 29, 31, 18, 16, 12, 10, 8]
led_on=0

for pin in LED_PINS:
  GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_PINS[led_on], GPIO.OUT, initial=GPIO.HIGH)

def next_led():
  global led_on
  GPIO.setup(LED_PINS[led_on], GPIO.OUT, initial=GPIO.LOW)
  led_on = (led_on + 1) % 10
  GPIO.setup(LED_PINS[led_on], GPIO.OUT, initial=GPIO.HIGH)
  

time.sleep(SLEEP_TIME)
while(True):
  next_led()
  time.sleep(SLEEP_TIME)

