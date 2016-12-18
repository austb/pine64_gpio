# LED projects

A collection of Pine 64 GPIO LED scripts.
The scripts must run as root in order to write to the files that control
the GPIO pins.

Genereal Usage:
```bash
$ sudo python script_name.py
```

## `blink_one.py`

Make an LED Blink using a Pine A64

### Setup

#### GPIO Pins

This script outputs through the PI-2-bus using pin 11 as its output pin
and pin 9 as its grounding pin.

#### Wiring

- The wire from pin 11 goes to the negative collum on a bread board.
- Coming out of another slot on the breadboard is a resistor (220 - 1k ohm
  will work)
  - This wire connects to a breadboard row
- In the same row of the breadboard as the resistor, insert the negative end
  of the led
- In an adjacent (DIFFERENT) row, insert the positive end of the LED
- In the same row as the positive end of the LED, connect the wire from pin 9

## Ten LED scripts

Scripts dealing with Ten LED's connected to the Pi-2 bus pins `[11, 13, 15, 29, 31, 18, 16, 12, 10, 8]`.
They also use two grounding pins (for example, 9 and 39).

### `blink_ten.py`

Make ten LED's blink in unison.

### `loop.py`

Make ten LED's blink in order. The wiring described below will result in the
sequence being a loop around the breadboard.

#### Setup

See setup diagram in `Pine64_10LED.pdf`.
