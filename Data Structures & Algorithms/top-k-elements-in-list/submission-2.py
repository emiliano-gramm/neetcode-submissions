class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = [[] for i in range(len(nums))]
        freq = defaultdict(int)
        finalRes = []

        for n in nums:
            freq[n] += 1

        for key, v in freq.items():
            res[v-1].append(key)
        
        ind = 0
        while (len(finalRes) < k):
            if res[::-1][ind]:
                for el in res[::-1][ind]:
                    finalRes.append(el)
            ind += 1
            print(finalRes)


        return finalRes

