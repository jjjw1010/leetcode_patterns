class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # Approach 1
        # # Boolean Array 
        # # O(n) Time with O(n) space
        # n = len(nums)
        # seen = [False for _ in range(n+1)]

        # for num in nums:
        #     if num >= 0 and num <= n:
        #         seen[num] = True

        # for i in range(1,len(seen)):
        #     if not seen[i]:
        #         return i
        # return n + 1

        # # Approach 2
        # # Hash Map
        # # Use input nums as a hashmap

        # # Clean Data
        # n = len(nums)
        # contains1 = False
        # for i in range(n):
        #     # Edge Case
        #     if nums[i] == 1:
        #         contains1 = True
        #     # Maintain numbers within [1,n]
        #     if nums[i] <= 0 or nums[i] > n:
        #         nums[i] = 1
        
        # if not contains1:
        #     return 1

        # # Use Data
        # for i in range(n):
        #     value = abs(nums[i])
        #     # Can't index nums[n] so nums[0] is saved for n
        #     if value == n:
        #         nums[0] = -abs(nums[0])
        #     else:
        #         nums[value] = -abs(nums[value])
        
        # # Output Data
        # # Checks value 1 to n - 1
        # for i in range(1, n):
        #     # Means value i hasn't been seen
        #     if nums[i] > 0:
        #         return i
        # # Checks value n
        # if nums[0] > 0:
        #     return n

        # return n + 1
        
        # Approach 3
        # Cycle Sort
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1