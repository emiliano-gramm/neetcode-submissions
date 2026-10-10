class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l = 0
        r = 0
        diff = prices[r] - prices[l]

        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
                r = i
            if prices[i] > prices[r]:
                r = i
            if prices[r] - prices[l] > diff:
                diff = prices[r] - prices[l]
        
        return diff