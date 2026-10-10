class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. could sort the strings
        #2. could make hashmaps of the strings (faster?)

        # hm1 = dict()
        # hm2 = dict()
        # for c in s:
        #     hm1[c] = 1 + hm1.get(c, 0)
        # for c in t:
        #     hm2[c] = 1 + hm2.get(c,0)
        # return hm1 == hm2

        #3. make use of array len 26, add and sub depending of string
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        base = ord('a')
        for i in range(len(s)):
            count[ord(s[i]) - base] += 1
            count[ord(t[i]) - base] -= 1
        for n in count:
            if n != 0:
                return False
        return True