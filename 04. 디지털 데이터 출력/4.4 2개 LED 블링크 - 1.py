from machine import Pin
import utime

led1 = Pin(26, Pin.OUT) # 26번 핀에 연결된 LED
led2 = Pin(27, Pin.OUT) # 27번 핀에 연결된 LED

INTERVAL1 = 300 # 점멸 간격
INTERVAL2 = 500

time_previous1 = utime.ticks_ms() # 기준 시간
time_previous2 = time_previous1

while True:
    time_current = utime.ticks_ms() # 현재 시간
    
    # 경과 시간 계산
    time_elapsed1 = utime.ticks_diff(time_current, time_previous1)
    time_elapsed2 = utime.ticks_diff(time_current, time_previous2)
    
    if time_elapsed1 >= INTERVAL1:
        time_previous1 = time_current # 기준 시간 변경
        led1.toggle() # LED1 반전
    if time_elapsed2 >= INTERVAL2:
        time_previous2 = time_current # 기준 시간 변경
        led2.toggle() # LED2 반전