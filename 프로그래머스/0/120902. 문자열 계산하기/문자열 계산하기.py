def solution(my_string):
    string= my_string.split()
    answer = int(string[0])
    for i in range(1,len(string),2):
        operator = string[i] # 연산자
        num = int(string[i+1]) # 숫자
        if operator == "+":
            answer += num
        elif operator == "-":
            answer -= num            
    return answer