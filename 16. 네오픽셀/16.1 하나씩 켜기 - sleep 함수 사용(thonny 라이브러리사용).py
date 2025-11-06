from machine import Pin
from neopixel import NeoPixel
from utime import sleep

number_pixel = 24
pin = Pin(18, Pin.OUT)
circle = NeoPixel(pin, number_pixel)

while True:
    for i in range(number_pixel):
        circle[i] = (255, 0, 0)
        circle.write()
        sleep(0.1)
        circle[i] = (0, 0, 0)
