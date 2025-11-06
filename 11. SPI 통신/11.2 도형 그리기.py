from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
from utime import sleep

spi = SPI(0, mosi=Pin(19), sck=Pin(18)) # 0번 SPI 포트 사용
# OLED 디스플레이 제어 객체 생성
# (width, height, spi, dc, rst, cs)
oled = SSD1306_SPI(128, 64, spi, Pin(17), Pin(20), Pin(16))

oled.fill(0) # 배경색으로 버퍼 채우기
oled.show() # 버퍼 내용을 화면에 나타내기

for x in range(0, 128, 4):
    oled.line(0, 0, x, 63, 1) # 직선 그리기
    oled.line(127, 0, 127-x, 63, 1)
    sleep(0.1)
    oled.show()