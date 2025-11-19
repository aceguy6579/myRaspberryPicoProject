from machine import Pin, PWM
from time import sleep

pin1 = Pin(19, Pin.OUT) # 모터 제어 핀 1
pin2 = Pin(18, Pin.OUT) # 모터 제어 핀 2

enable = PWM(Pin(20)) # 모터 활성화
enable.freq(15000) # PWM 주파수 설정
enable.duty_u16(0) # 모터 정지 상태

def set_duty(speed):
    global enable
    duty_min = int(65535 * 0.7) # 70% 듀티 사이클에서 최저 속도
    duty_max = int(65535 * 0.95) # 99% 듀티 사이클에서 최대 속도

    if speed == 0:
        duty = 0
    else:
        duty = int(duty_min + (duty_max - duty_min) * speed / 100)

    enable.duty_u16(duty)

def forward(speed=100):
    global pin1, pin2 # 전진
    set_duty(speed)
    pin1.value(0)
    pin2.value(1)

def backward(speed=100):
    global pin1, pin2 # 후진
    set_duty(speed)
    pin1.value(1)
    pin2.value(0)

def stop(speed=100):
    global pin1, pin2, enable # 정지
    enable.duty_u16(0)
    pin1.value(0)
    pin2.value(0)

mode = 0 # 정지(0), 저속, 중속, 고속(3)
mode_changed = False # 모드 변화 여부

# 모드 변화를 위한 버튼
up_btn = Pin(12, Pin.IN, pull=Pin.PULL_DOWN)
down_btn = Pin(13, Pin.IN, pull=Pin.PULL_DOWN)

up_previous = False # 모드가 증가 버튼의 이전 상태
down_previous = False # 모드가 감소 버튼의 이전 상태

up_current = False # 모드가 증가 버튼의 현재 상태
down_current = False # 모드가 감소 버튼의 현재 상태

print("시작")

while True:
    up_current = up_btn.value() # 모드 증가 버튼 상태 읽기
    down_current = down_btn.value() # 모드 감소 버튼 상태 읽기

    if up_current:
        if not up_previous: # LOW에서 HIGH로 변하는 상승 에지
            mode = mode + 1 # 모드 증가
            mode = min(mode, 3) # 고속에서 모드 증가 후 고속 유지
            mode_changed = True
    up_previous = up_current

    if down_current:
        if not down_previous: # LOW에서 HIGH로 변하는 상승 에지
            mode = mode - 1 # 모드 감소
            mode = max(mode, 0) # 정지에서 모드 감소 후에도 정지 유지
            mode_changed = True
    down_previous = down_current

    if mode_changed: # 모드가 바뀐 경우 회전 속도 변경
        mode_changed = False
        if mode == 0:
            stop()
            print("정지")
        elif mode == 1:
            forward(30)
            print("저속")
        elif mode == 2:
            forward(60)
            print("중속")
        else:
            forward(90)
            print("고속")