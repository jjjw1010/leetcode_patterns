class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Method 2: Traverse by Two Pointers (Floyd's Cycle Detection)
        slow, fast = nums[0], nums[0]

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
        
        # # Method 1: Traverse by Marking
        # # Traverse the array
        # for num in nums:
        #     idx = abs(num)
        #     # If number was previously marked,
        #     if nums[idx] < 0:
        #         # Return the number
        #         return idx
        #     # Mark nums[num] since all num is within [1, len(nums)] range
        #     # num can be used as an index
        #     nums[idx] *= -1
        