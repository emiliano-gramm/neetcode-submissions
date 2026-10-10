class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums) - 1

        while l<r:
            mid = l + (r-l)//2
            print(mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > nums[mid-1]:
                r = mid - 1
            else:
                break
        mid = l + (r-l)//2
        print(mid)
        return nums[mid] 