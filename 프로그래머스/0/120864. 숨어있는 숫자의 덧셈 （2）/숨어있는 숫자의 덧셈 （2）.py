def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        # 연속된 숫자인 경우를 위해 빈 문자열에 추가한다.
        if i.isdigit():
            num += i
        else:
            # 숫자인 경우가 끝난 경우 숫자를 더한다.
            if num:
                answer += int(num)
                num = ''
    # 마지막 숫자인 경우는 따로 계산한다.
    if num:
        answer += int(num)
    return answer