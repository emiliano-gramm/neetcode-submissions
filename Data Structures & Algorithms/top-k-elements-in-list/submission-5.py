from collections import deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = dict()

        for i in range(len(nums)):
            if nums[i] in container:
                container[nums[i]] += 1
            else:
                container[nums[i]] = 1

        checker = [[0, 0]]*k

        for k, v in container.items():
            for el in range(len(checker)):
                if v > checker[el][1]:
                    tempV = checker[el][1]
                    tempK = checker[el][0]
                    checker[el] = [k, v]
                    v = tempV
                    k = tempK
        finalRes = []
        for el in checker:
            finalRes.append(el[0])

        return finalRes
