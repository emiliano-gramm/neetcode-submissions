class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        inter = []
        
        intervals = sorted(intervals)

        curr = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            nMin = intervals[i][0]
            nMax = intervals[i][1]
            if (nMin <= curr[1] and nMin >= curr[0]) or (nMax >= curr[0] and nMax <= curr[1]) or (nMin <= curr[0] and nMax >= curr[1]):
                curr[0] = min(nMin, curr[0])
                curr[1] = max(nMax, curr[1])
            else:
                inter.append(curr)
                curr = [nMin, nMax]
        inter.append(curr)

        return inter
