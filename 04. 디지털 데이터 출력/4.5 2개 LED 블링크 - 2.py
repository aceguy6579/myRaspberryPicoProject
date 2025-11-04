from machine import Pin
import utime

#26번과 27번 핀에 연결괸 LED 리스트
leds = [Pin(26, Pin.OUT), Pin(27, Pin.OUT)]

INTERVAL = [300, 500] # 점멸 간격
time_previous = [utime.ticks_ms()] *2 # 기준 시간

while True:
    time_current = utime.ticks_ms() # 현재 시간
    
    for i, led in enumerate(leds):
        time_elapsed = utime.ticks_diff(time_current, time_previous[i])
        
        if time_elapsed >= INTERVAL[i]:
            time_previous[i] = time_current # 기준 시간 변경
            led.toggle() # LED 반전
