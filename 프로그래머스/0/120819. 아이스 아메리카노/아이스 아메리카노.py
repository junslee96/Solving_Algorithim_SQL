def solution(money):
    americano = money // 5500
    change = money % 5500
    answer = [americano, change]
    return answer