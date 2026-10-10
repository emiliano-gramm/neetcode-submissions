class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])
        i, e = 0, len(matrix)
        stopper = 0

        while (i < e and stopper < 10):
            midRow = i + (e-i)//2
            print(midRow)
            if matrix[midRow][0] > target:
                e = i + (e-i)//2
            elif matrix[midRow][0] <= target:
                if matrix[midRow][-1] >= target:
                    while(l < r and stopper < 10):
                        mid = l + (r-l)//2
                        print(mid, midRow, matrix[midRow][mid])
                        if matrix[midRow][mid] > target:
                            r = mid
                        elif matrix[midRow][mid] < target:
                            l = mid + 1
                        elif matrix[midRow][mid] == target:
                            return True
                        stopper += 1
                elif matrix[midRow][-1] < target:
                    i = i + (e-i)//2
                stopper += 1
        
        return False
                
