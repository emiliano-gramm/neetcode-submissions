class Solution:
    def isValid(self, s: str) -> bool:
        op = []

        for c in s:
            if c == "(" or c == "{" or c== "[":
                op.append(c)
            else:
                if len(op) > 0:
                    el = op.pop()
                    if not ((c == ")" and el == "(") or (c == "}" and el == "{") or (c == "]" and el == "[")):
                        return False
                else:
                    return False
        if len(op)>0:
            return False

        return True