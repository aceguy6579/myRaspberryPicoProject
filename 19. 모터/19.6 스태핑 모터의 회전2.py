from machine import Pin
from time import sleep

# 핀 설정
in1 = Pin(21, Pin.OUT)
in2 = Pin(20, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

pins = [in1, in4, in2, in3] # 역방향이 안됨: 순서를 바꿔가며 테스트

# 하프스텝(8단계) 제어 패턴
sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

# 속도 조절용 딜레이 (값이 작을수록 빠름)
delay = 0.002

while True:
    # 정방향 회전
    for _ in range(512):  # 반복 횟수 = 회전 각도 제어
        for step in sequence:
            for i in range(4):
                pins[i].value(step[i])
            sleep(delay)

    # 역방향 회전
    for _ in range(512):
        for step in reversed(sequence):
            for i in range(4):
                pins[i].value(step[i])
            sleep(delay)
