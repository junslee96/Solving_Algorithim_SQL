def solution(numbers):
    digits = list(numbers)
    used = [False] * len(digits)
    result_set = set()
    
    def generate(current):
        if current:
            result_set.add(int(''.join(current)))
        for i in range(len(digits)):
            if not used[i]:
                used[i] = True
                current.append(digits[i])
                generate(current)
                current.pop()
                used[i] = False
    generate([])
    
    count = 0
    for num in result_set:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
        
    return count