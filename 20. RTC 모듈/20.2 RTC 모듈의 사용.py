import utime
from machine import Pin, I2C
from ds3231_port import DS3231

sdaPIN = Pin(8) # 데이터 핀
sclPIN = Pin(9) # 클록 핀
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # 0번 I2C 포트 사용

ds3231 = DS3231(i2c) # RTC 모듈 제어 객체 생성

ds3231.save_time() # RTC 모듈 날짜와 시간 설정

while True:
    dateTime = ds3231.get_time() # 현재 날짜와 시간 얻기
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        dateTime[0], dateTime[1], dateTime[2], 
        dateTime[3], dateTime[4], dateTime[5]))
    utime.sleep(1)