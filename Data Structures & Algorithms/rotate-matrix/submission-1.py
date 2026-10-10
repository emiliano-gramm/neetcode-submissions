class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        """        #Do not try to do everything at the same time,
        #rotating 90 degrees is logically like transposing an putting in place.
        #Center in one first and then the other.

        #[3,0] -> [0,0], [2,0] -> [0,1], [1,0] -> [0,2], [0,0] -> [0,3]
        #[3,1] -> [1,0], [2,1] -> [1,1], [1,1] -> [1,2], [0,1] -> [1,3]
        #[3,2] -> [2,0], [2,2] -> [2,1], [1,2] -> [2,2], [0,2] -> [2,3]
        #[3,3] -> [3,0], [2,3] -> [3,1], [1,3] -> [3,2], [0,3] -> [3,3]

        save = [0,len(matrix) - 1]

        for row in range(len(matrix)):
            for col in range(row, len(matrix[row])):
               tmp = matrix[row][col]
               matrix[row][col] = matrix [col][row]
               matrix[col][row] = tmp

        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]"""



        l, r = 0, len(matrix) - 1

        while (l < r):
            for i in range(r-l):
                bottom, top = r, l

                leftTopCorner = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]

                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = leftTopCorner

            l += 1
            r -= 1