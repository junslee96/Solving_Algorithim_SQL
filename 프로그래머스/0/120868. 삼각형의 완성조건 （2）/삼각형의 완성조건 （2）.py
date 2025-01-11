def solution(sides):
    sides.sort()
    num1 = sides[0]
    num2 = sides[1]
    return (num1+num2) - (num2-num1) -1