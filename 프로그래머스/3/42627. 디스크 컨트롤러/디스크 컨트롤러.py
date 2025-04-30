import heapq

def solution(jobs):
    jobs = sorted([[s,l,i] for i, (s,l) in enumerate(jobs)],key=lambda x: x[0])
    heap = []
    time, total_time, idx, done = 0,0,0,0
    n = len(jobs)
    
    while done < n:
        while idx < n and jobs[idx][0] <= time:
            start, length, job_id = jobs[idx]
            heapq.heappush(heap, (length,start,job_id))
            idx += 1
        if heap:
            length, start, job_id = heapq.heappop(heap)
            time += length
            total_time += (time - start)
            done += 1
        else:
            time = jobs[idx][0]
    return total_time//n