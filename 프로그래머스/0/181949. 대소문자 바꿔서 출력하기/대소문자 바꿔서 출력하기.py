str = input()
result = ""
for char in str:
    if 'a' <= char <= 'z':
        result += chr(ord(char)-32)
    else:
        result += chr(ord(char)+32)
print(result)
    
