class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. could sort the strings
        #2. could make hashmaps of the strings (faster?)

        hm1 = dict()
        hm2 = dict()

        for c in s:
            hm1[c] = 1 + hm1.get(c, 0)

        for c in t:
            hm2[c] = 1 + hm2.get(c,0)

        return hm1 == hm2