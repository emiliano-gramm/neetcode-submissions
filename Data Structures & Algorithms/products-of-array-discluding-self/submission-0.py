class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nArr = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    nArr[i] *= nums[j]
        
        return nArr