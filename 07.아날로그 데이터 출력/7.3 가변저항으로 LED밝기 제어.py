from machine import Pin, PWM
import utime

analog_value = machine.ADC(1) # 1번 채널에 가변저항 연결
pwm = PWM(Pin(18)) # 16번 핀으로 PWM 신호 출력

pwm.freq(1000) # PWM 신호 주파수

while True:
    reading = analog_value.read_u16()
    pwm.duty_u16(reading)
    utime.sleep_ms(5)
