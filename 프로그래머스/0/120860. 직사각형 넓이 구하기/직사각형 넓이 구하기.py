def solution(dots):
    x_dots = [i[0] for i in dots]
    y_dots = [i[1] for i in dots]
    
    width = max(x_dots) - min(x_dots)
    depth = max(y_dots) - min(y_dots)
    
    return width * depth