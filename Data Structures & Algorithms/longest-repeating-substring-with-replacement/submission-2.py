class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for i in range(len(s)):
            j = i + 1
            c = s[i]
            temp = k
            while (j < len(s) and (s[j] == c or temp > 0)):
                if s[j] != c:
                    temp -= 1
                j += 1
            if j - i + temp > longest:
                longest = j - i + temp
                if j - i + temp > len(s):
                    return len(s)
        
        return longest
            
        