class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap solution
        maxHeap = [ -n for n in nums]
        heapq.heapify(maxHeap)

        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
            if k == 0:
                return -res