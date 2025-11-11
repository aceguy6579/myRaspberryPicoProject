from machine import Pin, UART, PWM

uart = UART(0, 9600)
pwm = PWM(Pin(2))
pwm.freq(1000)

while True:
    if uart.any():  # 수신 데이터가 있는 경우
        line = uart.readline()  # 한 줄 단위로 읽기
        if line:
            command = line.decode('utf-8').strip()  # \r\n 제거
            print('Received:', command)
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
