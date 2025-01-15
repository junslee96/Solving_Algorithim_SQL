def solution(bin1, bin2):
    decimal_sum = int(bin1,2) + int(bin2,2)
    
    return bin(decimal_sum)[2:]
