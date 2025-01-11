def solution(spell, dic):
    # 주어진 spell을 정렬하여 결합
    sorted_spell = ''.join(sorted(spell))
    
    for i in dic:
        if ''.join(sorted(i)) == sorted_spell:
            return 1
    return 2
        