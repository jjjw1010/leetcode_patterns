class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Idea
        # prod[curr] = left_total_prod * right_total_prod
        n = len(nums)
        left_prod = [1 for _ in range(n)]
        right_prod = [1 for _ in range(n)]

        for i in range(1,n):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]

        for i in range(n - 2, -1 , -1):
            right_prod[i] = nums[i + 1] * right_prod[i + 1]
            
        return [left_prod[i] * right_prod[i] for i in range(n)]
