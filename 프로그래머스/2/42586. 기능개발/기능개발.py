def solution(progresses, speeds):
    answer = []
    days_left = []
    
    for p, s in zip(progresses, speeds):
        import math
        days = math.ceil((100 - p) / s)
        days_left.append(days)
    
    count = 1
    max_days = days_left[0] 
    
    for i in range(1, len(days_left)):
        if days_left[i] > max_days:
            answer.append(count) 
            count = 1 
            max_days = days_left[i] 
        else:
            count += 1
    
    answer.append(count)
    
    return answer