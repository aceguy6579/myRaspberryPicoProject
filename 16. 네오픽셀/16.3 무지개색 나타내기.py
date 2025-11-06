from time import sleep
from neopixel import Neopixel

number_pixel = 24
circle = Neopixel(number_pixel, 0, 18, "GRB")
circle.brightness(10)

def rainbow(): # 무지개색 표현
    hue_step = 65536 // number_pixel # 65536를 픽셀 수로 나눔

    for i in range(number_pixel):
        # 65536 이상의 값이 나오는 경우 라이브러리에서 자동 조정
        current_hue = hue_step * i
        # (hue, saturation, value) 최대값 ( 65536, 255, 255)
        RGB_color = circle.colorHSV(current_hue, 255, 255)
        circle.set_pixel(i, RGB_color)
    circle.show()

rainbow()
while True:
    # 원형 버퍼와 같은 방법으로 오른쪽으로 지정한 픽셀만큼 픽셀값 회전
    circle.rotate_right(1)
    circle.show()
    sleep(0.1)