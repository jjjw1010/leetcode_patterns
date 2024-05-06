class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        diff = 0
        for i in range(n):
            diff += i - nums[i]
        return diff + n