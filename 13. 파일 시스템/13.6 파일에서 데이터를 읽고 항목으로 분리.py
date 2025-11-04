import os

FILE_NAME = 'student.txt' # 학생 정보 파일

file = open(FILE_NAME, 'r') # 읽기 모드로 열기
line = file.readline() # 줄 단위 읽기

while line:
    items = line.split(',') # 콤마를 기준으로 분할

    for item in items:
        print(item, '\t', end='')
    print()

    line = file.readline()

file.close() # 파일 닫기