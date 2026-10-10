class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        arr = []

        for i in range(len(strs)):
            arr.append(f'{len(strs[i])}#' + strs[i])
        print(arr)
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        arr = []
        if not s:
            return []

        index = 0
        nIndex = 0
        j = 0
        while (index < len(s)):
            while s[index + j] != "#":
                j += 1
            nIndex = index + int(s[index:index+j]) + j + 1
            print(index, nIndex, s[index+j+1:nIndex])
            arr.append(s[index+j+1:nIndex])
            index = nIndex #5Hello5World
            j = 0
        return arr