def solution(n):
    answer = []
    d = 2
    while d <= n: # 나누는 수가 n보다 커질때까지 반복
        if n% d == 0: # 약수 조건
            n/=d # 해당 약수 제외하기
            if d not in answer: # 해당약수가 중복인지 확인
                answer.append(d) # 중복이 아닐 경우 리스트에 추가
        else:
                d += 1 # 중복까지 확인 후 다음 차례로 이동
    return answer