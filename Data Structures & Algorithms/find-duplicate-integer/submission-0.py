class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])
            i+= 1
        return