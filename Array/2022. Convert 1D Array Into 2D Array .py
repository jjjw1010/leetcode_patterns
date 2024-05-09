class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        num_ele = len(original)
        ans = []
        if m * n != num_ele: 
            return ans
        
        for i in range(m):
            ans.append(original[i * n : i * n + n])
        return ans
            