import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SLEEP_TIME=0.3
LED_PINS = [11, 13, 15, 29, 31, 18, 16, 12, 10, 8]
led_is_on = False

for pin in LED_PINS:
  GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def toggle_led():
  global led_is_on
  if led_is_on:
    for pin in LED_PINS:
      GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    led_is_on=False
  else:
    for pin in LED_PINS:
      GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
    led_is_on=True

while(True):
  toggle_led()
  time.sleep(SLEEP_TIME)

