class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [1 2 3]
        # [4 5 6]
        # [7 8 9]
        # list(item) is functionally equivalent to [*item]
        # *item unpacks element in item
        # zip zips up by column
        if matrix:
            first_row = list(matrix.pop(0))
            remaining = list(zip(*matrix))[::-1]
            # *matrix -> [4,5,6],[7,8,9]
            # zip(*matrix) -> (4,7),(5,8),(6,9)
            # zip(*matrix)[::-1] -> (6,9),(5,8),(4,7)
            return first_row + self.spiralOrder(remaining)
        return []