from machine import Pin
from time import sleep

in1 = Pin(21, Pin.OUT) # 제어 핀을 출력으로 설정
in2 = Pin(20, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

pins = [in1, in2, in3, in4] # 제어 핀 리스트

# 분할각 단위의 회전을 위한 제어 패턴
sequence = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

while True:
    # 시계 방향 회전
    for _ in range(512): # 512회 4개 패턴 반복
        for i in range(4): # 512 * 4 = 2048스텝 1회전
            step = sequence[i]
            for j in range(len(pins)):
                pins[j].value(step[j])
                sleep(0.001)

    # 패턴 출력 순서를 반대로 하여 반시계 방향 회전
    for _ in range(512):
        for i in range(3, -1, -1):
            step = sequence[i]
            for j in range(len(pins)):
                pins[j].value(step[j])
                sleep(0.001)