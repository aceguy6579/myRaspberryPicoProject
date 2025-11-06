from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
import framebuf

spi = SPI(0, mosi=Pin(19), sck=Pin(18)) # 0번 SPI 포트 사용
# OLED 디스플레이 제어 객체 생성
# (width, height, spi, dc, rst, cs)
oled = SSD1306_SPI(128, 64, spi, Pin(17), Pin(20), Pin(16))

smile = bytearray( # 비트맵 패턴 데이터
    b'\x0F\xF0\x1F\xF8\x3F\xFC\x7F\xFE'
    b'\xE3\x87\xDD\x7B\xFF\xFF\xFF\xFF'
    b'\xFF\xFF\xFF\xFF\xEF\xF7\xF7\xEF'
    b'\x78\x1E\x3F\xFC\x1F\xF8\x0F\xF0'
)

# OLED 디스플레이에 표시할 FrameBuffer 클래스 객체 생성
fb = framebuf.FrameBuffer(smile, 16, 16, framebuf.MONO_HLSB)

oled.fill(0) # 배경색으로 버퍼 채우기
oled.blit(fb, 10, 10) # 비트맵 패턴 표시
oled.show()