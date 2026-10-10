class Solution:
    def isPalindrome(self, s: str) -> bool:
        point1 = len(s) - 1
        i = 0
        while (i < len(s)-1):
            while((i < len(s)-1 or point1 >= 0) and (not s[i].isalnum() or not s[point1].isalnum())):
                if not s[i].lower().isalnum():
                    i += 1
                if not s[point1].lower().isalnum():
                    point1-=1
            if (i < len(s)-1 or point1 >= 0) and s[i].lower() != s[point1].lower():
                return False
            point1 -= 1
            i += 1
            

        return True