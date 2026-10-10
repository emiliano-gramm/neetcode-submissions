class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r:int, c:int, grid: List[List[str]]):
            grid[r][c] = 0
            if r > 0 and grid[r-1][c] == "1":
                dfs(r-1,c,grid)
            if r < len(grid)-1 and grid[r+1][c] == "1":
                dfs(r+1,c,grid)
            if c > 0 and grid[r][c-1] == "1":
                dfs(r,c-1,grid)
            if c < len(grid[0])-1 and grid[r][c+1] == "1":
                dfs(r,c+1,grid)


        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c,grid)

        return islands





