import sys

data = sys.stdin.buffer.read().split()
# 처리 속도 개선을 위한 buffer 사용
# buffer : 입력을 바이트 단위로 읽을 수 있게 해주는 버퍼링된 바이너리 스트림

i = 1
stack = []
out = []
n = int(data[0])

while i < len(data):
    cmd = data[i]
    if cmd == b'1':
        x = int(data[i+1])
        stack.append(x)
        i += 2
    elif cmd == b'2':
        if stack:
            out.append(str(stack.pop()))
        else:
            out.append('-1')
        i += 1
    elif cmd == b'3':
        out.append(str(len(stack)))
        i += 1
    elif cmd == b'4':
        out.append('1' if not stack else '0')
        i += 1
    else:
        out.append(str(stack[-1]) if stack else '-1')
        i += 1
sys.stdout.write('\n'.join(out))