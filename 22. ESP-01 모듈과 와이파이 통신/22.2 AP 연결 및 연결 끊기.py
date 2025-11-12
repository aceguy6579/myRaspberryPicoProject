import myWiFi
from esp8266 import ESP8266
import utime

esp01 = ESP8266() # ESP-01 모듈 제어 객체 생성

print("StartUP : ", esp01.startUP())
print("Echo-OFF : ", esp01.echoING())
print("")

print("Firmware Version :")
print(esp01.getVersion())
print("")

# ESP-01 모듈의 와이파이 모드 확인
print("WiFi Current Mode :", esp01.setCurrentWiFiMode())
print("")

print("Try to connect with the WiFi...")
while(1):
    if "WIFI CONNECTED" in esp01.connectWiFi(myWiFi.ssid, myWiFi.pwd):
        print("ESP8266 connect with the WiFi...")
        break;
    else:
        print(".")
        utime.sleep(2)
print("")
print("Now you are connected...")
print("")

if esp01.disconnectWiFi():
    print("Disconnected...")
else:
    print("Problem during disconnection...")