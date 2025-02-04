# 단어 입력받기
S = input()

# 알파벳 a부터 z까지 순회하며 위치 확인
result = []
for char in range(ord('a'), ord('z') + 1):
    result.append(S.find(chr(char)))

# 결과 출력 (공백으로 구분)
print(" ".join(map(str, result)))
