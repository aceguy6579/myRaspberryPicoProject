import myWiFi
from esp8266 import ESP8266
import utime

def extract_data(response, field): # 필드 데이터 추출
    index_from = response.find('<' + field + '>')
    index_to = response.find('</' + field + '>')

    if index_from == -1 or index_to == -1:
        return "N/A"
    
    index_from += len('<' + field + '>')

    return response[index_from:index_to]

def print_info(response):
    date_time = extract_data(response, 'statusDt') # 기준 날짜
    print(date_time)

    decide_count = extract_data(response, 'hPntCnt') # 확진자수
    print('\t확진자 수\t: ' + decide_count)

    release_count = extract_data(response, 'dPntCnt') # 격리 해제수
    print('\t격리해제 수\t: ' + release_count)

    death_count = extract_data(response, 'gPntCnt') # 사망자수
    print('\t사망자 수\t: ' + death_count)

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

for count in range(10): 
    url = ("serviceKey=" + myWiFi.dataPortalKey + 
           "&pageNo=1"
           "&numOfRows=500"
           "&apiType=xml"
           "&status_dt=20200425"
           )

    # GET 방식의 HTTP 요청
    httpCode, httpRes = esp01.doHttpGet(
        "apis.data.go.kr", 
        "/1352000/ODMS_COVID_02/callCovid02Api?" + url
        )
    
    print("HTTP Code:", httpCode) # 응답 코드
    print("HTTP Response:", httpRes) # 응답 내용
    print("")

    print_info(httpRes) # 정보 출력

    utime.sleep(10) # 10초 간격으로 요청

if esp01.disconnectWiFi(): # 연결 끊기
    print("Disconnected...")
else:
    print("Problem during disconnection...")