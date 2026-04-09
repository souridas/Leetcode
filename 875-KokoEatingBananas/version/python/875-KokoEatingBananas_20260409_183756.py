# Last updated: 4/9/2026, 6:37:56 PM
1import math
2class Solution:
3    def minEatingSpeed(self, piles: List[int], h: int) -> int:
4        def check(k):
5            return sum([math.ceil(pile/k) for pile in piles])<=h
6        l=1
7        r=max(piles)
8        while l<r:
9            m=(l+r)//2
10            if check(m):
11                r=m
12            else:
13                l=m+1
14        return l
15            
16        