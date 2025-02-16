def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        arr_i = [arr[i] for i in range(s, e+1) if arr[i] > k]
        if arr_i:
            answer.append(min(arr_i))
        else:
            answer.append(-1)
    return answer
