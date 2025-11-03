import utime

rtc = machine.RTC()
rtc.datetime((2021, 12 ,25, 0, 12, 34, 56, 0))

while True:
    print(rtc.datetime())
    utime.sleep(1)