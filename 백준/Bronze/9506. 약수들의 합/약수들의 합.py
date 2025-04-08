test_cases = []

while True:
    n = int(input())
    if n == -1:
        break
    test_cases.append(n)

for n in test_cases:
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")