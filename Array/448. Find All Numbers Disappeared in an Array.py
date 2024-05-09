class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniq = set(nums)
        not_appear = []
        for i in range(1,len(nums) + 1):
            if i not in uniq:
                not_appear.append(i)
        return not_appear