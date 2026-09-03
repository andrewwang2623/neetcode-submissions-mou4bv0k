class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}
        seen[0] = nums[0]
        if len(nums) == 1:
            return seen[0]
        elif len(nums) == 2:
            return max(seen[0], nums[1])
        else:
            seen[1] = nums[1]
            seen[2] = nums[2] + seen[0]
            return max(self.helper(nums, len(nums)-2, seen), self.helper(nums, len(nums)-1, seen))
        
    def helper(self, nums, i, seen):
        # max money ending on i
        if i in seen:
            return seen[i]
        else:
            x = nums[i]
            money = x + max(self.helper(nums, i-3, seen), self.helper(nums, i-2, seen))
            seen[i] = money
            return money
