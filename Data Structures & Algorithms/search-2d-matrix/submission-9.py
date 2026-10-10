class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1 
        i, e = 0, len(matrix) - 1

        while (i <= e):
            midRow = i + ((e-i)//2)
            if matrix[midRow][0] > target:
                e = midRow - 1
            elif matrix[midRow][-1] < target:
                i = midRow + 1
            else:
                break

        while(l <= r):
            
            mid = l + ((r-l)//2)
            print(l, r, matrix[midRow][mid], target)
            if matrix[midRow][mid] > target:
                r = mid - 1
            elif matrix[midRow][mid] < target:
                l = mid + 1
            elif matrix[midRow][mid] == target:
                return True

        return False
                
