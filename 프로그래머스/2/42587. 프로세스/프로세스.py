from collections import deque

def solution(priorities, location):
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    count = 0
    
    while queue:
        current = queue.popleft()
        if any(x[0] > current[0] for x in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == location:
                return count
    return count
