def solution(before, after):
    if sorted(after) == sorted(before):
        return 1
    return 0