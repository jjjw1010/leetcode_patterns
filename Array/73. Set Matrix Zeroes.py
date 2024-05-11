class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []
        m = len(matrix)
        n = len(matrix[0])


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i,j))
        
        while(stack):
            i, j = stack.pop()
            for jj in range(n):
                matrix[i][jj] = 0
            for ii in range(m):
                matrix[ii][j] = 0
                 