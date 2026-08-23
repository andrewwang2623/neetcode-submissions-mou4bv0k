class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            if nums[len(nums) // 2] == target:
                return len(nums) // 2
            elif nums[len(nums) // 2] > target:
                return self.search(nums[0:(len(nums) // 2)], target)
            else:
                if self.search(nums[(len(nums) // 2 + 1):len(nums)], target) == -1:
                    return -1
                else:
                    return len(nums) // 2 + 1 + self.search(nums[(len(nums) // 2 + 1):len(nums)], target)