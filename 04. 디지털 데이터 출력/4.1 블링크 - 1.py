from machine import Pin # Pin 클래스 사용을 위해 포함
import utime # 시간 지연 함수를 위해 포함

led = Pin(25, Pin.OUT) # 내장 LED 연결 핀을 출력으로 설정

while True:
    led.value(1) # LED 켜기
    utime.sleep(0.5) # 0.5초 대기
    led.value(0) # LED 끄기
    utime.sleep_ms(500) # 0.5초 대기