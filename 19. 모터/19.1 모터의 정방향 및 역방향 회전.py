from machine import Pin, PWM
from time import sleep

pin1 = Pin(19, Pin.OUT) # 모터 제어 핀 1
pin2 = Pin(18, Pin.OUT) # 모터 제어 핀 2

enable = Pin(20, Pin.OUT) # 모터 활성화
enable.value(1) # HIGH를 출력, 모터를 제어 가능한 상태로

def forward():
    global pin1, pin2 # 전진
    pin1.value(0)
    pin2.value(1)

def backward():
    global pin1, pin2 # 후진
    pin1.value(1)
    pin2.value(0)

def stop():
    global pin1, pin2 # 정지
    pin1.value(0)
    pin2.value(0)

print('Forward...')
forward()
sleep(3)

print('Backward...')
backward()
sleep(3)

print('Stop...')
stop()