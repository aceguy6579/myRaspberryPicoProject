import machine
from utime import sleep

analog_value = machine.ADC(0)

while True:
    reading = analog_value.read_u16()
    print("ADC: ", reading)
    sleep(0.5)
