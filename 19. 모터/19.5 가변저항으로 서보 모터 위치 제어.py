from machine import Pin, PWM, ADC

# 나노초 단위의 펄스폭
MIN = 700000 # 0도에서의 펄스폭 : 0.7ms
MID = 1500000 # 90도에서의 펄스폭 : 1.5ms
MAX = 2300000 # 180도에서의 펄스폭 : 2.3ms

pwm = PWM(Pin(22))
pwm.freq(50) # PWM 신호의 주파수 설정

vr = ADC(0) # 0번 채널에 가변저항 연결

# 가변저항값을 서보 모터 제어를 위한 펄스폭으로 변환
def convert(x, in_min, in_max, out_min, out_max):
    return(x- in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    # 가변저항값을 16비트로 읽기
    reading = vr.read_u16()

    # PWM 신호를 위한 펄스폭으로 변환
    converted = convert(reading, 0, 65535, MIN, MAX)

    # 서보 모터 제어
    pwm.duty_ns(converted)