class Solution:
    def rob(self, nums: List[int]) -> int:
        
        total = 0
        loss = 0

        for i in range(len(nums)):
            best = nums[i]
            if i-3 in range(len(nums)):
                nums[i] = max(nums[i], nums[i]+nums[i-3], nums[i]+nums[i-2])
            elif i-2 in range(len(nums)):
                nums[i] = max(nums[i], nums[i]+nums[i-2])

        return max(nums)