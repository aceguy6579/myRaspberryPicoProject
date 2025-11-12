import myWiFi
from esp8266 import ESP8266

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

# GET 방식의 HTTP 요청
httpCode, httpRes = esp01. doHttpGet("www.google.com", "/")
print("HTTP Code:", httpCode) # 응답 코드
print("HTTP Response", httpRes) # 응답 내용

if esp01.disconnectWiFi(): # 연결 끊기
    print("Disconnected...")
else:
    print("Problem during disconnection...")