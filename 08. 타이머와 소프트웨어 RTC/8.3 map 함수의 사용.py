numbers_string = ['1', '2', '3', '4'] #문자열 리스트
print(numbers_string)

numbers = [0] * len(numbers_string) # 숫자 리스트
for i in range(len(numbers_string)): # 반복문을 사용한 변환
    numbers[i] = int(numbers_string[i])
print(numbers)

numbers = list(map(int, numbers_string)) # map 함수를 사용한 변환
print(numbers)