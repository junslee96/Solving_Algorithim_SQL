from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for name, count in participant_count.items():
        if count > completion_count.get(name, 0):
            return name