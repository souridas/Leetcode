# Last updated: 2/26/2026, 2:30:30 PM
1from collections import defaultdict
2class Solution:
3    def repeatedNTimes(self, nums: List[int]) -> int:
4        store=defaultdict(int)
5        for num in nums:
6            store[num]+=1
7        for k,v in store.items():
8            if v==len(nums)//2:
9                return k