def solution(clothes):
    clothes_dict = {}
    
    for name, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = [name]
        else:
            clothes_dict[kind].append(name)
    
    total_combinations = 1
    for count in clothes_dict.values():
        total_combinations *= (len(count) + 1)
        
    return total_combinations - 1