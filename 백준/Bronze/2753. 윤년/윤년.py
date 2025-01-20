#정수 입력
year = int(input())
#조건별로 나누기
if (year % 4 ==0 and year % 100 != 0) or year % 400 ==0:
    print(1)
else:
    print(0)