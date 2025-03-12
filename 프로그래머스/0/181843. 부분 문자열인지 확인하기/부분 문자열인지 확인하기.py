def solution(my_string, target):
    length = len(my_string) - len(target) + 1
    for i in range(length):
        if my_string[i:i+len(target)] == target:
            return 1
    return 0