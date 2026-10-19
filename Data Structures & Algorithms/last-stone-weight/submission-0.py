class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap
        maxHeap = [ -stone for stone in stones ]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)
            res = abs(s1-s2)
            if res:
                heapq.heappush(maxHeap, -res)
        
        return -maxHeap[0] if maxHeap else 0