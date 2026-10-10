class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nArr = [1] * len(nums)
        prefixArr = []
        postfixArr = []

        for i in range(len(nums)):
            postfixArr.append(nums[i+1:len(nums)])

        for i in range(len(nums)):
            prefixArr.append(nums[0:i])

        print(postfixArr, "aaa", prefixArr)

        for i in range(len(prefixArr)):
            for el in prefixArr[i]:
                if el != None:
                    nArr[i] *= el
        for i in range(len(postfixArr)):
            for el in postfixArr[i]:
                if el != None:
                    nArr[i] *= el

        return nArr