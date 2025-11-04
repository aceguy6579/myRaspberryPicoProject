from machine import Pin
import utime

led = Pin(25, Pin.OUT) # 내장 LED

time_previous = utime.ticks_ms()

while True:
    time_current = utime.ticks_ms() # 현재 시간
    time_elapsed = utime.ticks_diff(time_current, time_previous)
    if time_elapsed >= 500: # 0.5초 경과
        time_previous = time_current # 기준 시간 변경
        led.toggle() # LED 반전
