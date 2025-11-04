values = [0,1,2,3,4]

def handle_exception(index, denominator):
    try:
        devided = values[index] / denominator
        print(devided)
    except Exception as e:
        print("예외\t: ", e) # 예외 설명
        print("\t: ", type(e)) # 예외의 종류/클래스

handle_exception(2, 2) # 예외 발생하지 않음
handle_exception(5, 5) # 범위를 벗어난 인덱스 예외
handle_exception(3, 0) # 0으로 나누는 예외