class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two Pointer Question
        # Fast Pointer move everytime
        # Slow Pointer move conditionally
        #   In this case, when nums[slow] is not 0
        # When nums[slow] is zero and nums[fast] is not zero
        # you swap the two values

        slow = 0
        for fast in range(1, len(nums)):
            # When nums[slow] is initially zero,
            if nums[slow] == 0:
                # And nums[fast] is not zero
                if nums[fast] != 0:
                    # Perform the swap 
                    # [Put zero further back and ones front]
                    nums[slow], nums[fast] = nums[fast], nums[slow]
            # nums[slow] is preferably needs to be zero
            if nums[slow] != 0:
                slow += 1