import myWiFi
from esp8266 import ESP8266
import utime

def extract_data(response, field):  # 필드 데이터 추출
    start_tag = "<" + field + ">"
    end_tag = "</" + field + ">"

    index_from = response.find(start_tag)
    index_to = response.find(end_tag)

    if index_from == -1 or index_to == -1:
        return "N/A"

    index_from += len(start_tag)
    return response[index_from:index_to]

def print_info(response):
    date_time = extract_data(response, 'statusDt')  # 기준 날짜
    print(date_time)

    decide_count = extract_data(response, 'hPntCnt')  # 확진자 수
    print('\t확진자 수\t: ' + decide_count)

    release_count = extract_data(response, 'dPntCnt')  # 격리 해제 수
    print('\t격리해제 수\t: ' + release_count)

    death_count = extract_data(response, 'gPntCnt')  # 사망자 수
    print('\t사망자 수\t: ' + death_count)

    print("")

esp01 = ESP8266()

print("StartUP : ", esp01.startUP())  
print("Echo-Off : ", esp01.echoING())
print("")

print("Try to connect with the WiFi..")
while True:
    if "WIFI CONNECTED" in esp01.connectWiFi(myWiFi.ssid, myWiFi.pwd):
        print("ESP8266 connect with the WiFi..")
        break
    else:
        print(".")
        utime.sleep(2)

print("")
print("Now you are connected...")
print("")

print(httpRes)

for count in range(10):
    url = (
        "serviceKey=" + myWiFi.dataPortalKey +
        "&pageNo=1"
        "&numOfRows=500"
        "&apiType=xml"
        "&std_day=2020-04-25"
    )

    httpCode, httpRes = esp01.doHttpGet(
        "apis.data.go.kr",
        "/1352000/ODMS_COVID_02/callCovid02Api?" + url
    )

    print("HTTP Code:", httpCode)
    print("")

    print_info(httpRes)

    utime.sleep(10)

if esp01.disconnectWiFi():
    print("Disconnected...")
else:
    print("Problem during disconnection...")
