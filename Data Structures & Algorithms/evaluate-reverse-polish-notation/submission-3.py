class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = collections.deque()

        for i in range(len(tokens)):
            if tokens[i] in ["+", "/", "*", "-"]:
                el1 = s.pop()
                el2 = s.pop()
                print(el1,el2, tokens[i])
                if tokens[i] == "+":
                    nEl = el1+el2
                    s.append(nEl)
                elif tokens[i] == "-":
                    nEl = el2-el1
                    s.append(nEl)
                elif tokens[i] == "/":
                    nEl = int(el2/el1)
                    s.append(nEl)
                elif tokens[i] == "*":
                    nEl = el1*el2
                    s.append(nEl)
            else:
                s.append(int(tokens[i]))

        return s.pop()