import myWiFi
from esp8266 import ESP8266
import utime

def extract_data(response, field): # 필드 데이터 추출
    index_from = response.find('<' + field + '>')
    index_to = response.find('<' + field + '>')

    data = response[(index_from + 2 + len(field)):index_to]

    return data

def print_info(response):
    date_time = extract_data(response, 'stateDt') # 기준 날짜
    print(date_time)

    death_count = extract_data(response, 'deathCnt') # 사망자 수
    print('\t사망자 수\t: ' + death_count)

    decide_count = extract_data(response, 'decideCnt') # 확진자 수
    print('\t확진자 수\t: ' + decide_count)

    print("")

esp01 = ESP8266() # ESP-01 모듈 제어 객체 생성

print("StartUP : ", esp01.startUP()) # ESP-01 모듈과의 통신 검사
print("Echo-Off : ", esp01.echoING())
print("")

print("Try to connect with the WiFi..")
while(1): # 연결될 때까지 2초 간격으로 시도
    if "WIFI CONNECTED" in esp01.connectWiFi(myWiFi.ssid, myWiFi.pwd):
        print("ESP8266 connect with the WiFi..")
        break;
    else:
        print(".")
        utime.sleep(2)

print("")
print("Now you are connected...")
print("")

startCreateDate = "20211210" # 데이터 검색 시작 날짜
endCreateDate = "20211211" # 데이터 검색 끝 날짜

for count in range(10): # 10회 날씨 정보 요청
    # GET 방식의 HTTP 요청
    httpCode, httpRes = esp01.doHttpGet("openapi.data.go.kr")
    print("HTTP Code:", httpCode) # 응답 코드
    print("HTTP Response:", httpRes) # 응답 내용
    print("")

    print_info(httpRes) # 정보 출력

    utime.sleep(10) # 10초 간격으로 요청

if esp01.disconnectWiFi(): # 연결 끊기
    print("Disconnected...")
else:
    print("Problem during disconnection...")