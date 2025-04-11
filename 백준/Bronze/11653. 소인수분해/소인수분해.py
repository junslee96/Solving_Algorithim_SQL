N = int(input())
while N != 1:
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            print(i)
            N //= i
            break
    else:
        print(N)
        break
        