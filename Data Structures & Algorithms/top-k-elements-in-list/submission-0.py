class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ind = defaultdict(int)
        res = []

        for n in nums:
            ind[n] += 1

        i = 0
        while(i < k):
            max_k = max(ind, key=ind.get)
            res.append(max_k)
            ind[max_k] = -1
            i += 1
        
        return res
