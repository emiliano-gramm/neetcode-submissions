class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

#        def dfs(r:int, c:int):
#            grid[r][c] = "0"
#            if r > 0 and grid[r-1][c] == "1":
#                dfs(r-1,c,grid)
#            if r < len(grid)-1 and grid[r+1][c] == "1":
#                dfs(r+1,c,grid)
#            if c > 0 and grid[r][c-1] == "1":
#                dfs(r,c-1,grid)
#            if c < len(grid[0])-1 and grid[r][c+1] == "1":
#                dfs(r,c+1,grid)

        def bfs(r:int,c:int):
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == "1"):
                        q.append((r,c))
                        grid[r][c] = "0"
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    #dfs(r,c)
                    bfs(r,c)
                    islands += 1

        return islands





