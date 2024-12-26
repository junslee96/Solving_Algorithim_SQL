def solution(n):
    count = 0 # 합성수의 개수 구하기
    
    for num in range(2,n+1): # 2부터 n까지
        for i in range(2,num): # 2부터 num-1까지
            if num % i == 0: # 합성수의 조건
                count += 1
                break # 다음 num 순서로 넘기기
    return count