from machine import Pin, SPI
from PicoDHT22 import PicoDHT22
import sdcard
import os

WRITE_INTERVAL = 2 # 초 단위 로깅 시간 간격

# SPI 객체를 생성하고 이를 사용하여 SD 카드 객체 생성
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(13))

# SD 카드에 가상 파일 시스템(virtual file system, VFS) 생성
vfs = os.VfsFat(sd)

# SD 카드를 '/sd' 디렉터리로 마운트
os.mount(vfs, '/sdcard') # 파일 시스템 객체 사용

dht_sensor=PicoDHT22(Pin(22,Pin.IN,Pin.PULL_UP),dht11=True) # DHT22 온습도 센서를 위한 객체

def log_temp_humid(write_timer):
    # 추가 모드로 파일을 열어 파일 끝에 로깅 데이터 기록
    file = open("/sdcard/temp_humid.txt", "a")

    T, H = dht_sensor.read() # 온도와 습도 읽기
    if T is None:
        print("Sensor error")
    else:
        logging_data = "{}'C {}%".format(T, H)

        print(logging_data, end="\n")
        file.write(logging_data)
    
    file.close() # 파일 닫기

write_timer = machine.Timer() # 타이머 생성

# 지정한 시간 간격으로 로깅하도록 타이머 설정
write_timer.init(freq=(1/WRITE_INTERVAL),
                 mode=machine.Timer.PERIODIC, callback=log_temp_humid)

print("* Start Logging...") # 로깅 시작

while True:
    pass # 아무런 작업도 하지 않음