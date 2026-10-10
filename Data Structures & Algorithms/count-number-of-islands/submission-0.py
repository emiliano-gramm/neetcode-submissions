class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r:int, c:int, grid: List[List[str]], v: dict):
            v[(r,c)] = 1
            if r > 0 and not ((r-1,c) in v) and grid[r-1][c] == "1":
                dfs(r-1,c,grid,v)
            if r < len(grid)-1 and not ((r+1,c) in v) and grid[r+1][c] == "1":
                dfs(r+1,c,grid,v)
            if c > 0 and not ((r,c-1) in v) and grid[r][c-1] == "1":
                dfs(r,c-1,grid,v)
            if c < len(grid[0])-1 and not ((r,c+1) in v) and grid[r][c+1] == "1":
                dfs(r,c+1,grid,v)


        
        visited = {}
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(r,c)
                if grid[r][c] == "1" and not ((r,c) in visited):
                    islands += 1
                    dfs(r,c,grid,visited)
                    print("visited islands")
                    for k in visited:
                        print(k)

        return islands





