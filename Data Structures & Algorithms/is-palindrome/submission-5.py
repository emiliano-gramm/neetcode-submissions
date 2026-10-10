class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        point1 = len(s) - 1
        i = 0
        while (i < len(s)-1):
            while((i < len(s)-1 or point1 >= 0) and (not s[i].isalnum() or not s[point1].isalnum())):
                if not s[i].isalnum():
                    i += 1
                if not s[point1].isalnum():
                    point1-=1
            if (i < len(s)-1 or point1 >= 0) and s[i] != s[point1]:
                return False
            point1 -= 1
            i += 1
            

        return True