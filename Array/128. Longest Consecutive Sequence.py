class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Unique set of numbers
        num_set = set(nums)

        # Smallest nums list is [] so you start with 0
        sol = 0

        # Iterate each number
        for num in nums:
            # Find the smallest number/start of sequence
            if num - 1 not in num_set:
                # Find the length of that sequence
                next_num = num + 1
                while next_num in num_set:
                    next_num += 1
                # Compare this sequence length to the longest sequence length
                sol = max(sol, next_num - num)
        return sol
