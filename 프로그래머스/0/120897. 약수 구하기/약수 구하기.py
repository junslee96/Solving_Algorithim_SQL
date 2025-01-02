def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    answer.sort() 
    # 1부터 순서대로 추가되기 때문에 굳이 할 필요는 없다
    return answer