# Last updated: 4/10/2026, 3:44:12 PM
# heap
1import heapq
2class Solution:
3    def findKthLargest(self, nums: List[int], k: int) -> int:
4        heap=[]
5        for num in nums:
6            heapq.heappush(heap,-num)
7        while k-1:
8            heapq.heappop(heap)
9            k-=1
10        val=-heapq.heappop(heap)
11        return val
12        