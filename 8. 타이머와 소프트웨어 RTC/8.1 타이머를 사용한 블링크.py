from machine import Pin, Timer

led = Pin(25, Pin.OUT) # 내장 LED
LED_state = False # 꺼진 상태에서 시작
my_timer = Timer() # 타이머 객체 생성

# 콜백 함수, 콜백 함수를 호출한 Timer 클래스의 객체를 매개변수로 가짐
def blink(_timer):
    global led, LED_state # 전역변수 참조

    LED_state = not LED_state # LED 상태 반전
    led.value(LED_state)

# 1초에 한 번(freq)씩 반복해서(mode) 콜백 함수(callback) 호출
my_timer.init(mode=Timer.PERIODIC, freq=1, callback=blink)