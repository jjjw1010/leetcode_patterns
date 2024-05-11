class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Runs in O(n) but doesn't use constant extra space
        # used = set()
        # sol = []
        # for num in nums:
        #     if num in used:
        #         sol.append(num)
        #     else:
        #         used.add(num)
        # return sol       

        # Idea: The numbers are between 1 and n
        # Mark the used number as negative value
        # you do that by marking nums[abs(num) - 1] to be negative
        
        sol = []
        for num in nums:
            abs_num = abs(num)
            # If this number is marked
            if nums[abs_num - 1] < 0:
                sol.append(abs_num)
            
            # Mark this number because it is visited
            nums[abs_num - 1] *= -1
        return sol
