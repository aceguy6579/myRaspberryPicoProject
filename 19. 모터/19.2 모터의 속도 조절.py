from machine import Pin, PWM
from time import sleep

pin1 = Pin(19, Pin.OUT) # 모터 제어 핀 1
pin2 = Pin(18, Pin.OUT) # 모터 제어 핀 2

enable = PWM(Pin(20)) # 모터 활성화
enable.freq(15000) # PWM 주파수 설정
enable.duty_u16(0) # 모터 정지 상태

def set_duty(speed):
    global enable
    duty_min = int(65535 * 0.55) # 70% 듀티 사이클에서 최저 속도
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

print('Forward... Half Speed...')
forward(50)
sleep(2)

print('Forward... Full Speed...')
forward()
sleep(2)

print('Backward... Half Speed...')
backward(50)
sleep(2)

print('Backward... Full Speed...')
backward()
sleep(2)

print('Stop...')
stop()