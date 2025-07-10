array = [int(input()) for _ in range(5)]
array.sort()
print(round(sum(array)/len(array)))
print(array[2])