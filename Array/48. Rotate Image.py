class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Method 2: Better Method
        # Reverse and then Transpose = Rotation
        n = len(matrix)
        l = 0
        r = n - 1
        # Reverse
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # Transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # # Method # 1: Brute Force Rotation
        # # From outer to inner matrix 
        # # Top Left, Top Right, Bot Right, Bot Left = Bot Left, Top Left, Top Right, Bot Right
        # n = len(matrix)
        # for depth in range(n//2):
        #     for i in range(depth, n - 1- depth):
        #         # iterates left to right -> col changes
        #         top_left = matrix[depth][i]
        #         # iterates top to bottom -> row changes
        #         top_right = matrix[i][n - 1 - depth]
        #         # iterates right to left -> col changes
        #         bot_right = matrix[n - 1 - depth][n - 1 - i]
        #         # iterates bottom to top -> row changes
        #         bot_left = matrix[n - 1 - i][depth]

        #         # top_left, top_right, bot_right, bot_left
                
        #         # bot_left, top_left, top_right, bot_right
        #         matrix[depth][i], matrix[i][n - 1 - depth], matrix[n - 1 - depth][n - 1 - i], matrix[n - 1 - i][depth] = bot_left, top_left, top_right, bot_right

        