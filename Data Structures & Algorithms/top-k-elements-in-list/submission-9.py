class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = dict()

        for i in range(len(nums)):
            if nums[i] in container:
                container[nums[i]] += 1
            else:
                container[nums[i]] = 1

        tracker = [[] for _ in range(len(nums) + 1)]
        for key, val in container.items():
            tracker[val].append(key)

        res = []
        for i in range(len(tracker)-1, -1, -1):
            if tracker[i] != []:
                for val in tracker[i]:
                    res.append(val)
            if len(res) >= k:
                break
        return res