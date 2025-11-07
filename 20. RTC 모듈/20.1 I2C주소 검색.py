from machine import Pin, I2C

sdaPIN = Pin(8) # 데이터 핀
sclPIN = Pin(9) # 클록 핀

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # 0번 I2C 포트 사용

devices = i2c.scan() # 주소 검색

if len(devices) == 0:
    print('* No I2C device !')
else:
    print('* I2C devices found :', len(devices))

for device in devices: # 슬레이브 주소 출력
    print(" => HEX address : ", hex(device))