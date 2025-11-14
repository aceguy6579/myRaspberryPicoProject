import time, usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

count = 0

while True:
    count = count + 1

    keyboard_layout.write('Hello World~')
    keyboard_layout.write(str(count))
    keyboard_layout.write('\n')

    time.sleep(1)