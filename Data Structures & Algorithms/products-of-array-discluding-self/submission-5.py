class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lNums = [*nums]
        for i in range(1, len(nums)):
            lNums[i] = lNums[i-1] * nums[i]
        
        rNums = [*nums]
        for i in range(len(nums)-2, -1, -1):
            rNums[i] = rNums[i+1] * nums[i]

        for i in range(1, len(nums)-1):
            nums[i] = lNums[i-1] *rNums[i+1]
        nums[0] = rNums[1]
        nums[-1] = lNums[-2]

        return nums