import machine
from utime import sleep

# ADC3 핀을 입력으로 설정
ADC3_pin = machine.Pin(29, machine.Pin.IN)

vsys = machine.ADC(3) # 3번 채널 사용
# ADC값을 실제 전압으로 변환하기 위한 상수
VOLTAGE_CONVERSION = 3.3 * 3 / 65535

while True:
    reading = vsys.read_u16() # 16비트값으로 변환
    voltage = reading * VOLTAGE_CONVERSION # 실제 전압으로 변환

    print(voltage) # 전압 출력

    sleep(2) # 2초에 한번 출력