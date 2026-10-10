class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. could sort the strings
        #2. could make hashmaps of the strings (faster?)

        hm1 = dict()
        hm2 = dict()

        for c in s:
            if c in hm1:
                hm1[c] += 1
            else:
                hm1[c] = 1

        for c in t:
            if c in hm2:
                hm2[c] += 1
            else:
                hm2[c] = 1

        for k, e in hm1.items():
            print(k,e)

        for k, e in hm2.items():
            print(k,e)

        return hm1 == hm2