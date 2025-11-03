import utime

print()
print("             YYYY MM DD HH MM SS")
date_time = (input("Enter current date & time: ")) + ' 0 0'
# 기준 시간에서 입력한 시간까지 경과한 초 단위 시간
input_time = utime.mktime(list(map(int, tuple(date_time.split(' ')))))
# 현재 시스템 시간과 입력한 시간의 차이
time_delta = input_time - int(utime.time())

def timeNow():
    # 입력한 기준 시간을 사용하여 현재 시간을 날짜와 시간으로 변환하여 변환
    return utime.localtime(utime.time() + time_delta)

while True:
    dateTime = timeNow()
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        dateTime[0], dateTime[1], dateTime[2], 
        dateTime[3], dateTime[4], dateTime[5]))
    utime.sleep(1)