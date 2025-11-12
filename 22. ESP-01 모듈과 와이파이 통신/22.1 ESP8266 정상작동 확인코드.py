from esp8266 import ESP8266
esp01 = ESP8266()
# ESP-01 모듈에 AT 명령을 전송하여 참, 거짓 판단
print(f"StartUP: , {esp01.startUP()} \n")
# ESP-01 모듈의 펌웨어 버전 정보확인
print(f"{esp01.getVersion()} \n")
# ESP-01 모듈의 현재 Wi-Fi 동작 모드(STA, AP, 또는 STA+AP)를 설정하거나 확인
print(f"WiFi Current Mode : {esp01.setCurrentWiFiMode()} \n")

# ESP-01 모듈을 통해 주변의 Wi-Fi AP(Access Point, 즉 무선 네트워크)를 검색하여 리스트로 가져옴
aps = esp01.getAvailableAPs()
# 검색된 AP 목록을 순회 (인덱스 1부터 시작하는 이유: 0번은 헤더나 불필요한 데이터일 가능성 있음)
for i in range(1, len(aps)):
    ap = aps[i] # i번째 AP 정보 추출 (일반적으로 [SSID, RSSI, MAC, 암호화 방식] 형태)
    # 각 AP의 세부 정보 4개 항목을 쉼표로 구분하여 한 줄로 출력
    for j in range(4):
        print(ap[j] + ", ", end="")
    # 한 AP 정보 출력이 끝나면 줄바꿈
    print()