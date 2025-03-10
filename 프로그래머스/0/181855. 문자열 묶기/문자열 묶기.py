from collections import defaultdict

def solution(strArr):
    length_dict = defaultdict(int)
    for string in strArr:
        length_dict[len(string)] += 1
    return max(length_dict.values())