class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()

        split_size = (len(nums) - 1) // 2

        if len(nums) % 2:
            median = nums[split_size]
        else:
            median = (nums[int(split_size)] + nums[int(split_size) + 1]) / 2
        return median
