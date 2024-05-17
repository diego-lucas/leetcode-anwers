from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[], nums]
        for i in range(1, len(nums)):
            result.extend(combinations(nums, i))
        return result
