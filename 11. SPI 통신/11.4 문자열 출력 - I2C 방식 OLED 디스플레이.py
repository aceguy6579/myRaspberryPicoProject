from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq=400000) # I2C 포트 사용
print(i2c.scan()) # I2C 주소 검색

# I2C 객체의 설정 정보(사용 포트, SCL/SDA 핀, 주파수 등)를 문자열로 출력
print("I2C : " + str(i2c)) 

# OLED 디스플레이 제어 객체 생성
# (width, height, i2c, addr)
oled = SSD1306_I2C(128, 64, i2c, 0x3C)

oled.fill(0) # 배경색으로 버퍼 채우기
oled.show()

oled.text("Thank you", 10, 10) # 문자열 출력
oled.show()
