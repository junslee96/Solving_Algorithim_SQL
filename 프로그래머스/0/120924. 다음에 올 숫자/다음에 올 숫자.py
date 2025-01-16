def solution(common):
    # Geometric_Progression:등비수열
    # Arithmetic_Progression:등차수열
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        return common[-1] + diff
    else:
        ratio = common[1] // common[0]
        return common[-1] * ratio