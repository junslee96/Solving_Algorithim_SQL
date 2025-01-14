def solution(numlist, n): 
    # lambda 함수 : 익명 함수(anonymous function)
    # -> 이름이 없는 한 줄로 작성된 간단한 함수를 의미
    # "lambda 매개변수들 : 표현식"
    sorted_list = sorted(numlist, key=lambda x:(abs(x-n),-x))
    # -x : 거리가 같은 경우 더 큰 값을 우선
    # -> sorted가 오름차순 정렬이기 때문에 내림차순으로 바꾼 것
    return sorted_list
