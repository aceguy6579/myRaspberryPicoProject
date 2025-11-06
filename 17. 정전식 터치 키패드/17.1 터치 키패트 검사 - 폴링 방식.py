from machine import Pin, I2C
import time
import mpr121

i2c = I2C(0)
mpr = mpr121.MPR121(i2c, address=0x5A) # 터치 키패드 제어 객체

while True:
    state = mpr.touched() # 12개 센서 상태 읽기
    print('{0:5d}: '.format(state), end='')

for e in range(12): # 비트벼로 센서 상태 출력
    if state & (1 << e):
        print('0', end='')
    else:
        print('. ', end='')
    print()

    time.sleep(1)