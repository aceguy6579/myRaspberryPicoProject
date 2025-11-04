import os

def exists(path):
    try:
        os.stat(path) # 파일 또는 디렉터리 정보
        return True
    except OSError: # 존재하지 않는 파일 또는 디렉터리 예외
        return False
    
def check_existance(path):
    if(exists(path)):
        print('{0:>20} : Exist...'.format(path))
    else:
        print('{0:>20} : DOES NOT exist...'.format(path))


check_existance('hello5.py')
check_existance('i2c_lcd.py')
check_existance('lcd_api.py')
check_existance('lib')
check_existance('mpu6050.py')
check_existance('123.py')
check_existance('456.py')