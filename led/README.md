# Blinking LED

Make an LED Blink using a Pine A64

## Setup

### GPIO Pins

This script outputs through the PI-2-bus using pin 11 as its output pin
and pin 9 as its grounding pin.

### Wiring

- The wire from pin 11 goes to the negative collum on a bread board.
- Coming out of another slot on the breadboard is a resistor (220 - 1k ohm
  will work)
  - This wire connects to a breadboard row
- In the same row of the breadboard as the resistor, insert the negative end
  of the led
- In an adjacent (DIFFERENT) row, insert the positive end of the LED
- In the same row as the positive end of the LED, connect the wire from pin 9


