from machine import Pin, PWM
from time import sleep

# 나노초 단위의 펄스폭
MIN = 700000 # 0도에서의 펄스폭 : 0.7ms
MID = 1500000 # 90도에서의 펄스폭 : 1.5ms
MAX = 2300000 # 180도에서의 펄스폭 : 2.3ms

pwm = PWM(Pin(22))
pwm.freq(50) # PWM 신호의 주파수 설정

while True:
    pwm.duty_ns(MIN) # 0도 위치로 이동
    sleep(1)
    pwm.duty_ns(MID) # 90도 위치로 이동
    sleep(1)
    pwm.duty_ns(MAX) # 180도 위치로 이동
    sleep(1)