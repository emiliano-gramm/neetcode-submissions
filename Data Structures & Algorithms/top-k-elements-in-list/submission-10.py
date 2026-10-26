class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, [val, key])
            if len(heap) > k:
                element = heapq.heappop(heap)

        ans = []
        for el in heap:
            ans.append(el[1])

        return ans