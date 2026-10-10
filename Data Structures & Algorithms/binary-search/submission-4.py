class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = int((right-left)/2)

        while (left < right):
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            mid = left + int((right-left)/2)
            if nums[mid] == target:
                return mid
        
        if nums[mid] == target:
            return mid
        else:
            return -1