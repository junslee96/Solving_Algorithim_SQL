N = int(input().strip())

for _ in range(N):
    ps = input().strip()
    stack = []
    is_vps = True
    
    for ch in ps:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")