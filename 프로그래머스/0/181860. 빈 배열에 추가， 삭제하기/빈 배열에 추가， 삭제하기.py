def solution(arr, flag):
    result = []
    for i in range(len(arr)):
        if flag[i]:
            result.extend([arr[i]] * (arr[i] * 2))
        else:
            result = result[:-arr[i]] if arr[i] <= len(result) else []
    return result
