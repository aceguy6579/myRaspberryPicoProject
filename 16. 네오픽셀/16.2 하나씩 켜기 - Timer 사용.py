from machine import Timer
from neopixel import Neopixel

number_pixel = 24
circle = Neopixel(number_pixel, 0, 18, 'GRB')
circle.brightness(20) # 밝기(0~255)

position = 0
red_color = (255, 0, 0) # (R, G, B) 형식
off_color = (0, 0, 0)

my_timer = Timer()

def move_pixel(_timer):
    global position

    position = (position + 1) % number_pixel
    
    for i in range(number_pixel):
        if i == position: # 켜지는 픽셀
            circle.set_pixel(i, red_color)
        else: # 꺼지는 픽셀
            circle.set_pixel(i, off_color)
    circle.show()

# 초당 10회, 0.1초 간격으로 콜백 함수를 호출
my_timer.init(freq=10, mode=Timer.PERIODIC, callback=move_pixel)
