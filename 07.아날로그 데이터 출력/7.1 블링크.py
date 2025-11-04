from machine import Pin
import utime

INTERVAL = 500

led = Pin(16, Pin.OUT) # 16번 핀에 LED 연결

while True:
    led.value(1) # LED 켜기
    utime.sleep_ms(INTERVAL) # 0.5초 대기
    led.value(0) # LED 끄기
    utime.sleep_ms(INTERVAL) # 0.5초 대기