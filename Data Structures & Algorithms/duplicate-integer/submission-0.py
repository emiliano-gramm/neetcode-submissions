class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copNums = set(nums)
        return len(nums) != len(copNums)