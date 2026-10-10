class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mPath = 0
        tPath = 0
        dp = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                tPath = self.moveAround(row,col,matrix,dp)
                if tPath > mPath:
                    mPath = tPath
        
        return mPath


    def moveAround(self, ind_r, ind_c, matrix, dp):
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        tempPath = 1
        total_path = 1

        if (ind_r, ind_c) in dp:
            return dp[(ind_r, ind_c)]
        else:
            for x, y in directions:
                r = ind_r + x
                c = ind_c + y
                if r in range(len(matrix)) and c in range(len(matrix[ind_r])):
                    if matrix[r][c] > matrix[ind_r][ind_c]:
                        tempPath = 1 + self.moveAround(r,c,matrix, dp)
                    if tempPath > total_path:
                        total_path = tempPath
            dp[(ind_r, ind_c)] = total_path 
            return total_path


        
