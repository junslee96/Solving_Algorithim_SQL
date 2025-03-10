import math

def solution(arr):
    length = len(arr)
    
    next_power_of_two = 2 ** math.ceil(math.log2(len(arr)))
    
    zeros_to_add = next_power_of_two - length
    
    arr.extend([0] * zeros_to_add)
    
    return arr
