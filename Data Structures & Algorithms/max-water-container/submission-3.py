class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        mxSave = 0

        while l < r:
            crSave = (r-l) * min(heights[r],heights[l])
            if crSave > mxSave:
                mxSave = crSave
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return mxSave
