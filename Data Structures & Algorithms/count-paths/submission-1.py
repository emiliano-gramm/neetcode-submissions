class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if n == 1 and m == 1:
            return 1

        total = 0
        total = self.moveAround(m,n,0,0, total)
        return total


    def moveAround(self, m, n, r, c, total):

        q = collections.deque()
        q.append((r,c))
        while q:
            row, col = q.pop()
            directions = [[1,0], [0,1]]
            for d1, d2 in directions:
                n_row, n_col = row+d1, col+d2
                if n_row < m and n_col < n:
                    total = self.moveAround(m, n, n_row, n_col,total)
                if n_row == m-1 and n_col == n-1:
                    total += 1
        return total