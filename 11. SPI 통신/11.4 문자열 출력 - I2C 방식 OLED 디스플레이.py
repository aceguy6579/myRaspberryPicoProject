from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

sdaPIN = Pin(0)
sclPin = Pin(1)

i2c = I2C(0, sda=sdaPIN, scl=sclPin, freq=400000)
print("I2C scan result:", i2c.scan()) # I2C 주소 검색

# OLED 디스플레이 제어 객체 생성
# (width, height, i2c, addr)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# 초기화
oled.fill(0) # 배경색으로 버퍼 채우기
oled.text("Hello World~", 10, 10) # 문자열 출력
oled.text("I2C OLED Test", 10, 25) # 문자열 출력
oled.show()

# 간단한 카운트 예제
count = 0
while True:
    oled.fill_rect(0, 40, 128, 16, 0) # 이전 숫자 지우기(영역 덮어쓰기)
    oled.text("Count: {}".format(count), 10, 40)
    oled.show()
    count += 1
    sleep(1)