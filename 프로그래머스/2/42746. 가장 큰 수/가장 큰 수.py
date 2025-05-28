def solution(numbers):
    # 모든 정수를 문자열로 변환
    numbers = list(map(str,numbers))
    
    # 정렬 기준: 두 문자열을 붙였을 때 더 큰 조합이 앞에 오도록
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 모든 수를 이어붙임
    answer = ''.join(numbers)
    
    # 가장 큰 수가 0으로만 구성된 경우 ('000' 등), '0' 하나만 반환
    return '0' if answer[0] == '0' else answer
    return answer