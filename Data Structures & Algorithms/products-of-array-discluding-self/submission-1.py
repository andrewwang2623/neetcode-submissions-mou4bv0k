class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        leftprod = 1
        for i in range(len(nums)):
            val = nums[i]
            left.append(leftprod)
            leftprod *= val

        right = []
        rightprod = 1
        i = len(nums)-1
        while i > -1:
            val = nums[i]
            right.append(rightprod)
            rightprod *= val
            i -= 1

        for i in range(len(nums)):
            nums[i] = left[i] * right[len(nums)-i-1]
        return nums
        