def solution(array):
    # dict을 사용하여 각 숫자의 빈도 계산
    frequency = {}
    
    for num in array:
        #이미 존재하는 숫자의 빈도 1 증가
        if num in frequency:
            frequency[num] += 1
        #새로운 숫자일 경우 1로 초기화
        else:
            frequency[num] = 1
    
    # 최빈값의 최대 빈도수를 계산
    max_count = max(frequency.values())
    # dict 속에 최대 빈도수랑 같은 빈도를 가진 key값을 찾아 리스트로 변환
    modes = [key for key, val in frequency.items() if val == max_count]
    
    # 최빈값이 여러 개인 경우 -1로 반환
    if len(modes) > 1:
        return -1
    
    # 최빈값 반환
    return modes[0]