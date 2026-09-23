class Solution:
    import heapq

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]