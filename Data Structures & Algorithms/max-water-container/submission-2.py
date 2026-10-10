class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest = 0

        r = len(heights) - 1
        l = 0 

        while l < r:
            print(l,r)
            current = min(heights[l], heights[r]) * (r-l)
            if current > greatest:
                greatest = current

            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1

        return greatest