class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        copS = ""
        for c in s:
            if c.isalnum():
                copS += (c)

        return copS == copS[::-1]