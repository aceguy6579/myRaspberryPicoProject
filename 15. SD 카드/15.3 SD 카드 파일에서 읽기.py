# SD카드의 데이터를 안전하게 읽는 방법 (안전 제거 포함)

import machine, sdcard, os
from machine import SPI, Pin

# 1 SPI 및 SD카드 초기화
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(13))

# 2 SD카드 마운트
mount_point = "/sdcard"
os.mount(sd, mount_point)
print("SD카드가 성공적으로 마운트되었습니다.")

# 3 파일 읽기
file_name = mount_point + "/temp_humid.txt"

try:
    with open(file_name, "r") as f:
        print("파일 내용:")
        read_txt = f.read()
        print(read_txt)
except OSError as e:
    print("파일을 읽는 중 오류 발생:", e)

# 4 파일 시스템 언마운트
try:
    os.umount(mount_point)
    print("SD카드 언마운트 완료.")
except Exception as e:
    print("언마운트 실패:", e)

# 5 SPI 통신 해제
try:
    spi.deinit()
    print("SPI 통신 종료.")
except Exception as e:
    print("SPI 해제 실패:", e)

# 6 이제 SD카드를 안전하게 제거해도 됩니다.
print("이제 SD카드를 안전하게 제거할 수 있습니다.")
