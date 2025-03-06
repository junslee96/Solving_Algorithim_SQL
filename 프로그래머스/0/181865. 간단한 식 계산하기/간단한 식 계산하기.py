def solution(binomial):
    binomial_split = binomial.split()
    a,op,b = binomial_split
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b