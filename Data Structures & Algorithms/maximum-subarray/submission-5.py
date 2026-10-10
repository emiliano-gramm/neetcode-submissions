class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp = [*nums]

        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # return max(dp)

        #or

        maxSum = nums[0]
        curr = 0

        for n in nums:
            curr += n
            if curr > maxSum:
                maxSum = curr
            if curr < 0:
                curr = 0
        return maxSum
            


