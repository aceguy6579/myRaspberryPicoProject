from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT) # 내장 LED

while True:
    led.toggle() # LED 상태 반전
    sleep(0.5) # 0.5초 대기