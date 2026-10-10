class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        least = float('inf')
        res = []
        d = {}
        final = []

        heapq.heapify(res)
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = pow(0-x,2) + pow(0-y,2)
            heapq.heappush(res, (-distance,i))
            d[i] = [x,y]

        while len(res) > k:
            val, ind = heapq.heappop(res)
            del d[ind]

        for k, i in d.items():
            final.append(i)

        return final