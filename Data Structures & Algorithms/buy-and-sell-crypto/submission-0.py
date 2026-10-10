class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        slow = 0
        fast = 1

        minVal = prices[0]

        while (fast < len(prices)):
            if prices[fast] < minVal:
                slow = fast
                minVal = prices[fast]
            if profit < (prices[fast] - prices[slow]):
                profit = prices[fast] - prices[slow]
            
            fast += 1

        return profit
