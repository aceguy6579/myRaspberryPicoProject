from machine import Pin
from machine import I2C
from time import sleep
from i2c_lcd import I2cLcd

sdaPIN = Pin(0) # 데이터 핀
sclPIN = Pin(1) # 클록 핀

i2c = I2C(0, sda=sdaPIN, scl=sclPIN, freq=400000) # 0번 I2C 포트 사용

I2C_ADDR = i2c.scan()[0] if len(i2c.scan()) > 0 else 0x27 # 검색한 주소 중 첫 번째 주소

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16) # LCD 제어 객체

# 사용자 문자 정의
heart = bytearray([0x00, 0x0a, 0x1f, 0x1f, 0x0e, 0x04, 0x00, 0x00])
lcd.custom_char(0, heart) # 사용자 문자 등록

lcd.putstr(chr(0) + ' With My Heart ') # 사용자 문자 사용