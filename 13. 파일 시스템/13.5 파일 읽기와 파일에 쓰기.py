import os

FILE_NAME = 'number_date.log'

def exists(path):
    try:
        os.stat(path) # 파일 또는 디렉터리 정보
        return True
    except OSError: # 존재하지 않는 파일 또는 디렉터리
        return False
    
def checkLastNumber(fileName):
    file = open(fileName, 'r') # 읽기 모드로 파일 열기
    line = file.readline() # 줄 단위 읽기
    while line:
        count = int(line) # 문자열을 정수로 변환
        print(line.strip()) # 양쪽 끝 공백과 개행문자 제거
        line = file.readline() # 다음 줄 읽기
    file.close() # 파일 닫기

    return count

if exists(FILE_NAME):
    count = checkLastNumber(FILE_NAME)
else:
    count=0

file = open(FILE_NAME, 'a') # 추가로 쓰기 모드로 파일 열기
count = count + 1
print('Add Number : ', count)
file.write(str(count) + '\n')
file.close() # 파일 닫기