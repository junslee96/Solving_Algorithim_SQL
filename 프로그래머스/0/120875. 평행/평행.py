def solution(dots):
    #기울기 정의
    def slope(p1,p2):
        if p1[0] == p2[0]:
            return float('inf')
        return (p2[1]-p1[1]) / (p2[0]-p1[0])
    
    for i in range(len(dots)):
        for j in range(i+1,len(dots)):
            for k in range(len(dots)):
                for l in range(k+1,len(dots)):
                    #서로 다른 점 비교
                    if i != k and i != l and j != k and j != l:
                        if slope(dots[i], dots[j]) == slope(dots[k], dots[l]):
                            return 1
    return 0
