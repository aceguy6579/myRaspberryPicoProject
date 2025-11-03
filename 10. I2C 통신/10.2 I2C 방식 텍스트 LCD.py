from machine import Pin
from machine import I2C
from time import sleep_ms
from i2c_lcd import I2cLcd

sdaPIN = Pin(0) # 데이터 핀
sclPIN = Pin(1) # 클록 핀

i2c = I2C(0, sda=sdaPIN, scl=sclPIN, freq=400000) # 0번 I2C 포트 사용

I2C_ADDR = i2c.scan()[0] if len(i2c.scan()) > 0 else 0x27 # 검색한 주소 중 첫 번째 주소

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16) # LCD 제어 객체

count = 0
lcd.clear() # LCD 지우기
lcd.putstr('Count : ') # 문자열 출력

while True:
    lcd.move_to(8, 0) # 커서 위치 이동
    lcd.putstr("     ")
    lcd.move_to(8, 0)
    lcd.putstr(str(count))
    count += 1
    sleep_ms(1000)