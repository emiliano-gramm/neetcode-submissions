class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[None]"
        arr = []
        for s in range(len(strs)-1):
            arr.append(strs[s]+'[sep]')
        arr.append(strs[-1])
        return "".join(arr)
    def decode(self, s: str) -> List[str]:
        if s == "[None]":
            return []
        arr = s.split('[sep]')
        return arr