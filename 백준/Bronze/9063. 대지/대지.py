n=int(input())
points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

x_values = [x for x,y in points]
y_values = [y for x,y in points]

x_diff = max(x_values) - min(x_values)
y_diff = max(y_values) - min(y_values)

print(x_diff*y_diff)