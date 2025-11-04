import os, time

file_list = os.listdir() # 파일과 디렉터리 리스트

for file in file_list:
    print('{0:<13}'.format(file), end='') # 이름 출력

    info = os.stat(file) # 파일 또는 디렉터리 정보
    m_time = time.localtime(info[7]) # 수정한 날짜와 시간

    if info[0] == 0x8000: # 파일
        print('FILE : ', end='')
    elif info[0] == 0x4000: # 디렉터리
        print('DIR : ', end='')

    print('{0:04d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'
          .format(m_time[0], m_time[1], m_time[2],
                  m_time[3], m_time[4], m_time[5]), end='')
    
    if info[0] == 0x8000: # 파일인 경우 크기 출력
        print(', SIZE : ', end='')
        print(info[6])
    elif info[0] == 0x4000:
        print()