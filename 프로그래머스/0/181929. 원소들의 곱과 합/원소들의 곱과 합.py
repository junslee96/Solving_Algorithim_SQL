def solution(num_list):
    sum = 0
    product = 1
    for i in num_list:
        sum += i
        product *= i
    if sum**2  > product:
        return 1
    else:
        return 0