class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-size for size in stones]
        print(heap)
        heapq.heapify(heap)

        while len(heap) > 1:
            m1 = -heapq.heappop(heap)
            m2 = -heapq.heappop(heap)
            if m1>m2:
                heap.append(-(m1-m2))
            elif m1<m2:
                heap.append(-(m2-m1))
            
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0