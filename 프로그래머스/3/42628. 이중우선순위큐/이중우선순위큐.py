import  heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        if op.startswith("I"):
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
        elif op == "D 1":
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val)
                heapq.heapify(min_heap)
                
        elif op == 'D -1':
            if min_heap:
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
                heapq.heapify(max_heap)
                
    if not min_heap:
        return [0,0]
    else:
        return [-max_heap[0], min_heap[0]]