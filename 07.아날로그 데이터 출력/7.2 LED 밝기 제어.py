from machine import Pin, PWM
import utime

pwm = PWM(Pin(16)) # 16번 핀으로 PWM 신호 출력

pwm.freq(1000) # PWM 신호 주파수 지정

while True:
    for duty in range(65536): # 0~65535: 점점 밝게
        pwm.duty_u16(duty)
        utime.sleep_us(1)

    for duty in range(65534, 0, -1): # 65534~1: 점점 어둡게
        pwm.duty_u16(duty)
        utime.sleep_us(1)
