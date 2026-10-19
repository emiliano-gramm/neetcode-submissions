class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        if len(s) == 1:
            return 1
        l = 0
        r = 0

        alp = [-1] * 200



        mLen = 0

        alp[ord(s[0])] = 0

        while r < len(s) - 1:
            r += 1

            if alp[ord(s[r])] >= 0 and alp[ord(s[r])] + 1 > l:
                l = alp[ord(s[r])] + 1
            alp[ord(s[r])] = r

            cLen = r - l + 1
            if cLen > mLen:
                mLen = cLen
        return mLen