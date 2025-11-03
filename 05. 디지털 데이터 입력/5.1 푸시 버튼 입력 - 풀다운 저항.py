from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT) # 내장 LED
# 16번 핀에 푸시 버튼 연결, 내장 풀다운 저항 사용
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    btn_status = button.value() # 푸시 버튼 상태 읽기
    led.value(btn_status) # 푸시 버튼의 값으로 LED 설정