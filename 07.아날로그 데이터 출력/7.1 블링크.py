from machine import Pin
import utime

INTERVAL = 500

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    utime.sleep_ms(INTERVAL)
    led.value(0)
    utime.sleep_ms(INTERVAL)