class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        elements = list(frequencies.keys())
        elements.sort(key=lambda num: frequencies[num], reverse=True)
        return elements[:k]