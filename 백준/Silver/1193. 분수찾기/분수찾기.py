X = int(input())
line = 1
count = 1

while count + line <= X:
    count += line
    line += 1

position = X - count
if line % 2 == 1:
    numerator = line - position
    denominator = 1 + position
else:
    numerator = 1 + position
    denominator = line - position
print(f"{numerator}/{denominator}")
