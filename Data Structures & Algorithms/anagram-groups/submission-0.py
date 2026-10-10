class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        nStrs = []

        for i in range(len(strs)):
            k = "".join(sorted(strs[i]))
            if k in hashMap:
                nStrs[hashMap[k]].append(strs[i])
            else:
                hashMap[k] = len(hashMap)
                nStrs.append([strs[i]])
        

        return nStrs