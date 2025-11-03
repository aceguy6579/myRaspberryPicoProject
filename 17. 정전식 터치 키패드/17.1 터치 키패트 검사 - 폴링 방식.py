from machine import Pin, I2C
import time
import mpr121

i2c = I2C(0)
mpr = mpr121.MPR121(i2c)

while True:
    state = mpr.touched()
    print('{0:5d}: '.format(state), end='')

for e in range(12):
    if state & (1 << e):
        print('0', end='')
    else:
        print('. ', end='')
    print()

    time.sleep(1)