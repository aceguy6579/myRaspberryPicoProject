from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=17, echo_pin=16) # 객체 생성

while True:
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm') # 거리 측정
    except OSError as ex: # 거리 측정 실패시
        print('ERROR getting distance:', ex)

    time.sleep(1)