class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        used = set()
        for i in range(len(nums)):
            if nums[i] not in used:
                for pair in self.twoSum(nums, -nums[i], i):
                    print(pair)
                    if pair[0] > i and pair[1] > i:
                        triplets.append([nums[i]] + [nums[j] for j in pair])
                used.add(nums[i])
        return triplets


    def twoSum(self, nums, target, used):
        pairs = []
        seen = {}
        seenAgain = set()
        for i in range(len(nums)):
            if i != used:
                if target-nums[i] in seen:
                    pairs.append([i, seen[target-nums[i]]])
                    seen.pop(target-nums[i])
                    seenAgain.add(nums[i])
                    seenAgain.add(target-nums[i])
                elif nums[i] not in seenAgain:
                    seen[nums[i]] = i
        return pairs