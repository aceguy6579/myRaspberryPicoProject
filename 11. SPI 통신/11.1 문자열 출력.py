from machine import Pin, SPI
from ssd1306 import SSD1306_SPI

spi = SPI(0, mosi=Pin(19), sck=Pin(18)) # 0번 SPI 포트 사용
# OLED 디스플레이 제어 객체 생성
# (width, height, spi, dc, rst, cs)
oled = SSD1306_SPI(128, 64, spi, Pin(17), Pin(20), Pin(16))

oled.fill(0) # 배경색으로 버퍼 채우기
oled.show() # 버퍼 내용을 화면에 나타내기

oled.text("Hello World~", 10, 10) # 문자열 출력
oled.show() # 버퍼 내용을 화면에 나타내기