def solution(emergency):
    sorted_emer= sorted(emergency, reverse=True)
    sequence_dict={}

    for sequence, value in enumerate(sorted_emer, start =1):
        sequence_dict[value] = sequence
    answer = [sequence_dict[value] for value in emergency]
    return answer