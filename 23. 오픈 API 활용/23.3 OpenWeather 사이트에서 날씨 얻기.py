import myWiFi
from esp8266 import ESP8266
import utime
import json

def print_info(response):
    pos_start = response.find('{') # 왼쪽부터 찾기
    pos_end = response.rfind('}') # 오른쪽부터 찾기

    # 중괄호로 시작해서 중괄호로 끝나도록 자르기
    response = response[pos_start:(pos_end+1)]

    # JSON 형식 데이터를 사전(dict) 형식으로 변환
    parsed = json.loads(response)

    print('Location : ' + parsed.get('name'))
    # 캘빈온도(절대온도) 반환
    print('Temperatuer : ' + '{0:.2f}'.format(parsed.get('main').get('temp') - 273.15))

    # 대괄호 내의 내용은 리스트로 변환되고
    # 리스트 내 중괄호 내의 내용은 사전 형식으로 봔환
    weather = parsed.get('weather') # 리스트 반환
    print('Weather : ' + weather[0].get('description'))
    print("")

esp01 = ESP8266() # ESP-01 모듈 제어 객체 생성

print("StartUP : ", esp01.startUP()) # ESP-01 모듈과의 통신 검사
print("Echo-Off : ", esp01.echoING())

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

for count in range(10): # 10회 날씨 정보 요청
    # GET 방식의 HTTP 요청
    httpCode, httpRes = esp01.doHttpGet("api.openweathermap.org",
                                        "/data/2.5/weather?id=1841808&appid=" + myWiFi.weatherKey)
    print("HTTP Code:", httpCode) # 응답 코드
    print("HTTP Response:", httpRes) # 응답 내용
    print("")

    print_info(httpRes) # 정보 출력

    utime.sleep(10) # 10초 간격으로 요청

if esp01.disconnectWiFi(): # 연결 끊기
    print("Disconnected...")
else:
    print("Problem during disconnection...")