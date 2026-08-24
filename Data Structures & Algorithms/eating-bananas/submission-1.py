class Solution:
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            val = self.hours(piles, mid)
            if val <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left

    
    def hours(self, piles: List[int], k: int) -> int:
        sum = 0
        for pile in piles:
            sum += math.ceil(pile / k)
        return sum