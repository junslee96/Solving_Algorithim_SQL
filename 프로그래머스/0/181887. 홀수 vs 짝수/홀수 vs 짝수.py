def solution(num_list):
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            odd += int(num_list[i])
        else:
            even += int(num_list[i])
    return even if even > odd else odd