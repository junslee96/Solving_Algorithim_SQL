import sys

def is_balanced(line: str) -> bool:
    stack = []
    pairs = {')':'(', ']':'['}
    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch in ')]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

def main():
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        if line == '.':
            break
        print("yes" if is_balanced(line) else "no")
       
    
if __name__ == "__main__":
    main()