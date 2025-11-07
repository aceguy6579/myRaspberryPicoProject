from machine import Pin
from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=17, echo_pin=16) # 객체 생성
buzzer = Pin(22, Pin.OUT) # 버저 연결 핀

THRESHOLD = 15 # 버저 동작을 위한 임계치
state_previous = False # 이전 버저 상태

while True:
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm') # 거리 측정

        if distance <= THRESHOLD: # 물체가 임계치 내로 들어오고
            if state_previous == False: # 버저가 정지 상태이면
                buzzer.value(1) # 버저 동작
                print("Buzzer ON !")
            state_previous = True # 버저 동작 상태
        else: # 물체가 임계치 밖으로 벗어나고
            if state_previous == True: # 버저가 동작 상태이면
                buzzer.value(0) # 버저 정지
                print("Buzzer OFF !")
            state_previous = False
    except OSError as ex: # 거리 측정 실패
        print('ERROR getting distance:', ex)
    
    time.sleep(0.5)