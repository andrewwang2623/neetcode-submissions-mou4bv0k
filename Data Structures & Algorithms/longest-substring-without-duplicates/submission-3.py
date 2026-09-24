class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 0
        longest = 1
        current_letters = set(s[0])
        while right < len(s) - 1:
            right += 1
            if s[right] in current_letters:
                while s[right] in current_letters:
                    current_letters.remove(s[left])
                    left += 1
            current_letters.add(s[right])
            if right - left + 1> longest:
                longest = right - left + 1
        return longest