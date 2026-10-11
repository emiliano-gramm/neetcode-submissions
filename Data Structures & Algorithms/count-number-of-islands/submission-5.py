class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        explored = dict()

        def dfs(r, c):
            if (r,c) in explored:
                return 0
            else:
                explored[(r,c)] = 1
                directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                if r in range(0, len(grid)) and c in range(0,len(grid[0])) and grid[r][c] != '0':
                    for d in directions:
                        dfs(d[0], d[1])
                    return 1
                return 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != '0':
                    islands += dfs(r,c)

        return islands