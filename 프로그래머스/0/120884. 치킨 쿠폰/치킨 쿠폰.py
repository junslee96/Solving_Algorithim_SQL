def solution(chicken):
    service = 0
    while chicken >= 10:
        service += 1
        chicken -= 9    
    return service