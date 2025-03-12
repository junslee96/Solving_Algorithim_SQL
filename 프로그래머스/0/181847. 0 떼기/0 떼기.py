def solution(n_str):
    for i in range(len(n_str)):
        if not n_str[i] == '0':
            return n_str[i:]