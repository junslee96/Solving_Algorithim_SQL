def solution(order):
    result = 0
    for num in order:
        if 'americano' in num or 'anything' in num:
            result += 4500
        elif 'latte' in num:
            result += 5000
    return result