def solution(num_list):
    result = 0
    for i in range(len(num_list)):
        while num_list[i] != 1:
            if num_list[i] % 2 == 0:
                num_list[i]/=2
                result += 1
            elif num_list[i] % 2 == 1:
                num_list[i] = (num_list[i]-1)/2
                result += 1            
    return result