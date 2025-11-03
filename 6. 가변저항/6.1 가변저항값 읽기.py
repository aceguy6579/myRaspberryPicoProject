import machine
from utime import sleep

analog_value = machine.ADC(0) # 0번 채널에 가변저항 연결

while True:
    reading = analog_value.read_u16() # 16비트값으로 반환
    print("ADC: ", reading)
    sleep(0.5)