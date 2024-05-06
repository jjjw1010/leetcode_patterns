class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique_dict = set(nums)
        return len(unique_dict) != len(nums)
