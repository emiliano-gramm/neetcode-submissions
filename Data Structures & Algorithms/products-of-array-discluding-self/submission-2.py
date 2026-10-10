class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nArr = [1] * len(nums)
        prefixArr = []
        postfixArr = []

        curr = 1
        for i in range(len(nums)):
            nArr[i] = curr
            curr *= nums[i]

        nCurr = 1
        for i in range(len(nums)-1, -1, -1):
            nArr[i] *= nCurr
            nCurr *= nums[i]

        return nArr