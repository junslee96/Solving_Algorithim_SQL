def solution(arr):
    x = 0 
    while True:
        prev_arr = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1        
        if prev_arr == arr:
            break        
        x += 1    
    return x