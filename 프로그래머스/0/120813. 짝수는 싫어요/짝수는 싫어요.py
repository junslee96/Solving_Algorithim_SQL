def solution(n):
    n_odd=[]
    # 정수 n 이하의 홀수만 추출하여 리스트 변환
    for i in range(1,n+1,2):
        n_odd.append(i)
    return n_odd
