class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l = 0
        r = 0
        diff = prices[r] - prices[l]

        while r < len(prices):
            # move left pointer if we find lower price, but r cannot be < l
            if prices[r] < prices[l]:
                l = r
            #check if current price difference is greater than before
            diff = max(diff, prices[r] - prices[l])

            r+=1
        
        return diff