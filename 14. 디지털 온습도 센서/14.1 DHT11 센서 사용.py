from machine import Pin
from PicoDHT22 import PicoDHT22
from utime import sleep

dht_sensor=PicoDHT22(Pin(22,Pin.IN,Pin.PULL_UP),dht11=True)

while True:
    T, H = dht_sensor.read() # 온도와 습도 읽기
    if T is None:
        print("Sensor error")
    else:
        print("{}'C {}%".format(T, H))

    sleep(1) # DHT11을 위해서는 최소 1초 간격 필요