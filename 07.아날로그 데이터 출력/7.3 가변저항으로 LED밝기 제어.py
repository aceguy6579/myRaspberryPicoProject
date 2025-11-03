from machine import Pin, PWM
import utime

analog_value = machine.ADC(1)
pwm = PWM(Pin(18))

pwm.freq(1000)

while True:
    reading = analog_value.read_u16()
    pwm.duty_u16(reading)
    utime.sleep_ms(5)
