# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            actual = nums[i]
            nums[i] = None
            needed = target - actual
            if needed in nums:
                return [i, nums.index(needed)]


nums = [3,2,4]
target = 6

print(Solution().twoSum(nums, target))