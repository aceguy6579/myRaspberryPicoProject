import time
import machine
import onewire, ds18x20

data = machine.Pin(18) # 온도 센서 연결 핀
temp_wire = onewire.OneWire(data) # 1-와이어 통신을 위한 객체

temp_sensors = ds18xx20.DS18X20(temp_wire) # 온도 센서 제어를 위한 객체

roms = temp_sensors.scan() # 온도 센서 검색
print(len(roms), 'temperature sensors found.')

while True:
    print('Temperatures:', end='')
    temp_sensors.convert_temp() # 온도를 변환하여 센서 내에 저장
    time.sleep(1) # 온도 변환을 윟나 대기시간 최대 750ms

   for rom in roms: # 온도 출력
        t = temp_sensors.read_temp(rom)
        print('{:>6.2f}'.format(t), end='')
    print()