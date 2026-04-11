# Last updated: 4/11/2026, 10:38:12 AM
# normal heap
1from collections import defaultdict
2import heapq
3class Solution:
4    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
5        store=defaultdict(int)
6        heap=[]
7        for num in nums:
8            store[num]+=1
9            heapq.heappush(heap,(-store[num],num))
10        ans=[]
11        while heap:
12            freq,num=heapq.heappop(heap)
13            if num not in ans:
14                ans.append(num)
15            if len(ans)==k:
16                return ans
17        return []
18            
19
20
21        