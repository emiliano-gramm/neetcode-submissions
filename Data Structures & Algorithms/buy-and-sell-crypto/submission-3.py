class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l = 0
        r = 0
        diff = prices[r] - prices[l]

        for i in range(len(prices)):
            # move left pointer if we find lower price, but r cannot be < l
            if prices[i] < prices[l]:
                l = i
                r = i
            # if greater price found then r should be there
            if prices[i] > prices[r]:
                r = i
            #check if current price difference is greater than before
            if prices[r] - prices[l] > diff:
                diff = prices[r] - prices[l]
        
        return diff