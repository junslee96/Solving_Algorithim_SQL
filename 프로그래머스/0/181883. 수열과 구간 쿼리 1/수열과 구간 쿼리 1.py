def solution(arr, queries):
    for i in range(len(queries)):
        for num in range(queries[i][0],queries[i][1]+1):
            arr[num] += 1
    return arr