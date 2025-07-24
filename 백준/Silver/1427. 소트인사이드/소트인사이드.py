num=input().strip()
digits=[int(d) for d in num]
digits.sort(reverse=True)
result=''.join(str(d) for d in digits)
print(result)