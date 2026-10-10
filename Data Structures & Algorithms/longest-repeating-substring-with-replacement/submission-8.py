class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        longest = 0
        l = 0
        for i in range(len(s)):
            hashMap[s[i]] += 1
            
            while (i-l+1) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1
            
            longest = max(longest, i-l+1)

        return longest
            
        