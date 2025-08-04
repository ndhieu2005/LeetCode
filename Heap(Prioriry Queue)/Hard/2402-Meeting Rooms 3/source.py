class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)] # 0,1,2,3....
        busy = [] #(end_time,start_time)
        count = [0] *n 
        
        for start,end in meetings:
            while busy and start >= busy[0][0]:
                _,room = heapq.heappop(busy)
                heapq.heappush(free,room)
            
            if not free:
                end_time , room = heapq.heappop(busy)
                end = end_time + (end - start)
                heapq.heappush(free,room)
            
            room = heapq.heappop(free)
            heapq.heappush(busy,(end,room))
            count[room] += 1
        return count.index(max(count))




        