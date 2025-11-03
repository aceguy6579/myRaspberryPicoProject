import utime
from machine import Pin
from machine import UART # UART 통신을 위한 클래스

computer = UART(0, timeout = 100) # 0번 UART 포트 사용, 0.1초 대기시간

while True:
    count = computer.any() # 수신 버퍼 검사
    if count > 0:
        str_bytes = computer.readline() # 세 줄 문자까지 읽기
        # 바이트 스트링을 문자열로 변환
        str_unicode = str_bytes.decode('UTF-8')
        print(str_bytes) # 셀로 bytes 형식 문자열 출력
        # UART 통신으로 컴퓨터로 변환된 문자열 출력
        computer.write('=> ' + str_unicode)w