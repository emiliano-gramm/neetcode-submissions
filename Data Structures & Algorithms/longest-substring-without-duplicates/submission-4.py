class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            currLongest = s[l:r]
            if s[r] in hashMap:
                l = max(hashMap[s[r]] + 1, l)
            longest = max(longest, r-l+1)
            hashMap[s[r]] = r
            

        return longest