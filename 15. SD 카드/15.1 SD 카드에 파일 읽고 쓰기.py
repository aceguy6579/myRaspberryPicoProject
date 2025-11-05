from machine import Pin, SPI
import sdcard
import os

# SPI 객체를 생성하고 이를 사용하여 SD 카드 객체 생성
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(13))

# SD 카드에 가상 파일 시스템(virtual file system, VFS) 생성
vfs = os.VfsFat(sd)

# SD 카드를 '/sd' 디렉터리로 마운트
os.mount(vfs, '/sdcard') # 파일 시스템 객체 사용
# os.mount(sd, '/sdcard') # SD 카드 객체를 사용해서도 마운트 가능

print(os.listdir('/sdcard')) # 디렉터리 내 파일 목록 출력

file = open("/sdcard/sample.txt", "w") # 쓰기 모드로 열기

for i in range(5): # 파일에 문자열 쓰기
    file.write("Sample text = %s\r\n" % i)

file.close() # 파일 닫기

file = open("/sdcard/sample.txt", "a") # 추가 모드로 열기
file.write("Appended at the END \n") # 파일 끝에 문자열 추가
file.close() # 파일 닫기

file = open("/sdcard/sample.txt", "r") # 읽기 모드로 열기
if file != 0:
    print("Reading from SD card")
    read_date = file.read()
    print(read_date)

file.close()