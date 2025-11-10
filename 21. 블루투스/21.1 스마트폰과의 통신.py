from machine import Pin, UART, Timer
uart = UART(0, 9600, timeout=100) # 0번 UART 포트
bt_timer = Timer() # 타이머 객체 생성

count = 0 # 2초에 1씩 증가하는 카운터

def send_count(_timer): # 콜백 함수
    globar = count

    count = count + 1 # 카운터값 1 증가
    uart.write(str(count)) # 블루트스 모듈을 통해 스마트폰으로 전송
    uart.write('\r\n')

# 2초에 한 번(freq)씩 반복해서(mode) 콜백 함수(callback) 호출
bt_timer.init(mode=Timer.PERIODIC, freq=0.5, callback=send_count)

while True:
    if uart.any(): # 수신 데이터가 있는 경우
        command = uart.readline()
        print(command.decode('UTF-8'), end='')