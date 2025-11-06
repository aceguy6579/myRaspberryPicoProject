from utime import sleep
from neopixel import Neopixel

number_pixel = 24
circle = Neopixel(number_pixel, 0, 18, 'GRB')
circle.brightness(20) # 밝기(0~255)

position = 0
red_color = (255, 0, 0)
off_color = (0, 0, 0)

while True:
    position = (position + 1) % number_pixel
    
    for i in range(number_pixel):
        if i == position: # 켜지는 픽셀
            circle.set_pixel(i, red_color)
        else: # 꺼지는 픽셀
            circle.set_pixel(i, off_color)
    circle.show()

sleep(0.1)
