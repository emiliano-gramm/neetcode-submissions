class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        area = 0
        maxArea = 0

        def dfs(grid, i, j, area):
            grid[i][j] = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for r, c in directions:
                row, col = i+r, j+c
                if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                    area = 1 + dfs(grid, row, col, area)
            return area
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 1
                    area = dfs(grid, i, j, area)
                    if area > maxArea:
                        maxArea = area

        
        return maxArea