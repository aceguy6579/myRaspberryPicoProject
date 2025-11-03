import utime
from machine import Pin
from machine import UART # UART 통신을 위한 클래스

computer = UART(0) # 0번 UART 포트 사용

LED = Pin(25, Pin.OUT) # 내장 LED
LED.value(0) # LED는 꺼진 상태에서 시작

while True:
    LED.toggle() # LED 상태 반전
    utime.sleep(0.5) # 0.5초 대기
    # UART 연결을 사용하여 컴퓨터로 메시지 출력
    computer.write('Toggle LED...' + str(LED.value()) + '\n')