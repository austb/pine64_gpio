import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_PIN = 11
led_is_on = False

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

def toggle_led():
  global led_is_on
  if led_is_on:
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    led_is_on=False
  else:
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)
    led_is_on=True

while(True):
  toggle_led()
  time.sleep(0.3)

