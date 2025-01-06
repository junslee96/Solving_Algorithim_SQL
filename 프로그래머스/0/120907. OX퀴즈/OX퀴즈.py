def solution(quiz):
    answer = []
    for i in quiz:
        quiz_1 = i.split()
        X = int(quiz_1[0])
        Y = int(quiz_1[2])
        Z = int(quiz_1[4])
        operator = quiz_1[1]
        
        if operator == '+':
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")
        else:
            answer.append("O" if X - Y == Z else "X")
    return answer
