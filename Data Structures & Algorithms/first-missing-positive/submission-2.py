class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        least = 1

        for i in range(len(nums)):
            if least in setNums:
                least += 1
            else:
                break
        
        return least