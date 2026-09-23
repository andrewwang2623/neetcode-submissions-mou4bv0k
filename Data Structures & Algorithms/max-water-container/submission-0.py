class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        max_size = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            size = min(left_height, right_height) * (right - left)
            if size > max_size:
                max_size = size
            if left_height > right_height:
                right = right - 1
            else:
                left = left + 1
        return max_size
