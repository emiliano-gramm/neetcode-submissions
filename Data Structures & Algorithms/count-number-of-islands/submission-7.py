from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()

        def dfs(r, c):
            q = deque()
            q.append((r,c))
            directions = [[1,0], [-1,0], [0,-1], [0,1]]
            while q:
                curr = q.pop()
                for d in directions:
                    nRow, nCol = curr[0]+d[0], curr[1]+d[1]
                    if nRow in range(len(grid)) and nCol in range(len(grid[r])) and (nRow,nCol) not in seen and grid[nRow][nCol] == "1":
                        q.append((nRow, nCol))
                        seen.add((nRow, nCol))
            return 1

        
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    seen.add((r,c))
                    total += dfs(r, c)

        return total