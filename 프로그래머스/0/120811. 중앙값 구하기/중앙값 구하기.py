def solution(array):
    n = len (array) # 리스트의 길이 계산
    answer = sorted(array)[n//2] 
    # sorted() : 입력 리스트를 오름차순으로 정렬
    # 중간 인덱스 위치를 2로 나눈 몫으로 계산
    return answer