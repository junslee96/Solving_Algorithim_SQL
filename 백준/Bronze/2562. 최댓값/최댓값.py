numbers=[]
for i in range(9):
    n=int(input())
    numbers.append(n)
max_value=max(numbers)
max_index=numbers.index(max_value)+1
print(max_value)
print(max_index)