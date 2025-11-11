from machine import Pin, UART, PWM

uart = UART(0, 9600) # 0번 UART 포트

command = '' # 듀티 사이클을 저장할 변수
process = False # 수신 문자열 처리 여부
pwm = PWM(Pin(25)) # LED 연결 핀
pwm.freq(1000)

while True:
    if uart.any(): # 수신 데이터가 있는 경우
        data = uart.read(1).decode('UTF-8')
        
        if data in ['\r', '\n']:
            if command:
                process = True
        else:
            command += data

        if process: # 듀티 사이클 수신이 끝나면 처리
            print('Received : ', command)
            try:
                duty_cycle = int(command)
                if 0 <= duty_cycle <= 100:
                    pwm.duty_u16(int(655.35 * duty_cycle))
                    print(duty_cycle, '% brightness')
                    uart.write(str(duty_cycle) + '% brightness\r\n')
                else:
                    uart.write('Wrong input... (0~100)\r\n')
            except ValueError:
                uart.write('Invalid input\r\n')
                
            command = ''
            process = False