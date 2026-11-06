class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for i in range(1, len(prices)):
            value = prices[i] - prices[l]
            if value > profit:
                profit = value
            if prices[i] < prices[l]:
                l = i
        
        return profit