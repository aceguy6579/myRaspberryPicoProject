import utime
from machine import Pin, I2C
from ds3231_port import DS3231
from PicoDHT22 import PicoDHT22

sdaPIN = Pin(8) # 데이터 핀
sclPIN = Pin(9) # 클록 핀
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # 0번 I2C 포트 사용

dht11 = PicoDHT22(Pin(2)) # DHT 온습도 센선 제어 객체 생성
ds3231 = DS3231(i2c) # RTC 모듈 제어 객체 생성

# ds3231.save_time() # RTC 모듈 날짜와 시간 설정

while True:
    dateTime = ds3231.get_time() # 현재 날짜와 시간 얻기

    temp = ds3231.get_temperature() # DS3231 칩 온도
    T, H = dht11.read() # 주변 온도와 습도

    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} : {:.2f}, {:.2f}".format(
        dateTime[0], dateTime[1], dateTime[2], 
        dateTime[3], dateTime[4], dateTime[5], temp, T))
    utime.sleep(2)
