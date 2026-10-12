class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        bestGuess = 1
        worstGuess = len(nums)

        for i in range(len(nums)):
            if bestGuess in nums:
                bestGuess += 1
            else:
                break
        
        return bestGuess