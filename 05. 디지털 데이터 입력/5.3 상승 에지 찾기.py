from machine import Pin
import utime

button_state_previous = False
button_state_current = False

led = Pin(25, Pin.OUT) # 내장 LED
button = Pin(16, Pin.IN, Pin.PULL_DOWN) # 16번 핀에 푸시 버튼 연결

count = 0

while True:
    button_state_current = button.value() # 푸시 버튼 상태 읽기
    if button_state_current: # 현재 상태가 HIGH이고
        if not button_state_previous: # 이전 상태가 LOW이면 상승에지
            count = count + 1
            # utime.sleep(0.1) # 디바운싱
            led.toggle() # LED 상태 반전
            print(count)
    button_state_previous = button_state_current