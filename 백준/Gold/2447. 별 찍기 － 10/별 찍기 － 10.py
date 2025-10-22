def draw_star(n):
    if n == 1:
        return ['*']
    prev = draw_star(n//3)
    result = []
    for p in prev:
        result.append(p*3)
    for p in prev:
        result.append(p+' '*(n//3)+p)
    for p in prev:
        result.append(p*3)
    return result
n = int(input())
print('\n'.join(draw_star(n)))