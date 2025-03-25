word = input()
n = len(word)
for i in range(n):
    if word[i] == '=' or word[i] == '-':
        if word[i-1]=='z' and word[i-2]=='d' and word[i] =='=':
            n-=2
        else:
            n -= 1
    elif word[i] == 'j':
        if word[i-1] == 'l' or word[i-1] == 'n':
            n -= 1
print(n)