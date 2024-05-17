class Solution:
    def canJump(self, nums: List[int]) -> bool:

        size = len(nums)
        target = size - 1
        for i in range(target,-1,-1):
            if i + nums[i] >= target:
                target = i
        if target == 0:
            return True
        return False
