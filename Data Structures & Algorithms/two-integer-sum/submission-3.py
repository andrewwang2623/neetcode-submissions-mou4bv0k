class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i in range(len(nums)):
            if nums[i] in targets:
                if (i < targets[nums[i]]):
                    return [i, targets[nums[i]]]
                else:
                    return [targets[nums[i]], i]
            else:
                targets[target-nums[i]] = i