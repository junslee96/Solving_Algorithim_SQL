import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while scoville:
        least = heapq.heappop(scoville)
        if least >= K:
            return count
        if not scoville:
            return -1
        second_least = heapq.heappop(scoville)
        new_food = least + (second_least * 2)
        heapq.heappush(scoville, new_food)
        count += 1
    return -1