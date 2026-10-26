class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = [["0" for _ in range(26)] for _ in range(len(strs))]

        for i in range(len(strs)):
            for c in strs[i]:
                words[i][ord(c) - ord("a")] += "1"

        container = defaultdict(list)
        for i in range(len(words)):
            currWord = "".join(words[i])
            container[currWord].append(strs[i])

        finalAns = []
        for k, v in container.items():
            finalAns.append(v)
        return finalAns