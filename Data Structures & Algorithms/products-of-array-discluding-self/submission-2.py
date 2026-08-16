class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        leftprod = 1
        for i in range(len(nums)):
            val = nums[i]
            left.append(leftprod)
            leftprod *= val

        rightprod = 1
        i = len(nums) - 1

        while i > -1:
            val = nums[i]
            nums[i] = left[i] * rightprod
            rightprod *= val
            i -= 1

        return nums
        