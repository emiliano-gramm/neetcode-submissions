class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        l, r = 0,0

        currLongest = s[l:r]
        longest = currLongest

        for i in range(len(s)):
            r += 1
            currLongest = s[l:r]
            if s[i] in hashMap:
                l = max(hashMap[s[i]] + 1, l)
                currLongest = s[l:r]
            if len(currLongest) > len(longest):
                longest = currLongest
            hashMap[s[i]] = i
            print(currLongest, l,r)
            

        return len(longest)
            