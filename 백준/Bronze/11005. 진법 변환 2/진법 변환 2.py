N,B = map(int,input().split())

alpha = {i:chr(i + ord('A')-10) for i in range(10,36)}
result = ''
while N > 0:
    remainder = N % B
    if remainder<10:
        result = str(remainder) + result
    else:
        result = alpha[remainder] + result
    N = N // B
print(result)