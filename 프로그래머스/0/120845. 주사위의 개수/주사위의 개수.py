def solution(box, n):
    width = box[0] // n #가로
    depth = box[1] // n #세로
    height = box[2] // n #높이
    answer = width*depth*height
    return answer