import machine
from utime import sleep

sensor_temp = machine.ADC(4)
VOLTAGE_CONVERSION = 3.3 / 65535 # 실제 전압으로 변환하기 위한 상수

while True:
    reading = sensor_temp.read_u16()
    voltage = reading * VOLTAGE_CONVERSION # 실제 전압
    # 전압에서 온도 변환을 위한 식
    temperature = 27 - (voltage - 0.706) / 0.001721

print(temperature)

sleep(2)