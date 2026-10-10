class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        if len(s1) > len(s2):
            return False
        
        for c in s1:
            arr1[ord(c)-ord('a')] += 1

        j = 0

        for i in range(len(s2)):
            if i-j+1 > len(s1):
                arr2[ord(s2[j])-ord('a')] -= 1
                j += 1
            arr2[ord(s2[i]) - ord('a')] += 1
            if arr2 == arr1:
                return True
        
        return False


            