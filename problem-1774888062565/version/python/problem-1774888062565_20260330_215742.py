# Last updated: 3/30/2026, 9:57:42 PM
# simple dict
1from collections import defaultdict
2class Solution:
3    def minAbsoluteDifference(self, nums: list[int]) -> int:
4        collector=defaultdict(list)
5        for i,num in enumerate(nums):
6            if num==1 or num==2:
7                collector[num].append(i)
8        ans=float('inf')
9        if len(collector)<2:
10            return -1
11        for i in collector[1]:
12            for j in collector[2]:
13                ans=min(ans,abs(i-j))
14        return ans
15        