def solution(polynomial):
    # 다항식을 공백 기준으로 분리
    terms = polynomial.split(' + ')
    
    # 계수 초기화
    x_coeff = 0
    constant = 0

    # 각 항을 처리
    for term in terms:
        if 'x' in term:  # x항 처리
            if term == 'x':
                x_coeff += 1  # 계수가 생략된 경우
            else:
                x_coeff += int(term[:-1])  # 계수를 추출하여 더함
        else:  # 상수항 처리
            constant += int(term)

    # 결과 문자열 생성
    result = []
    if x_coeff == 1:
        result.append('x')  # 계수가 1일 경우 '1x' 대신 'x'
    elif x_coeff:
        result.append(f'{x_coeff}x')
    if constant:
        result.append(str(constant))

    return ' + '.join(result)