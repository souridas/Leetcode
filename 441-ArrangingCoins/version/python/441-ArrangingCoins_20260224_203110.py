# Last updated: 2/24/2026, 8:31:10 PM
# k(k+1)//2 binary search
1class Solution:
2    def arrangeCoins(self, n: int) -> int:
3        l,h=0,n
4        ans=0
5        while l<=h:
6            m=(l+h)//2
7            if m*(m+1)//2<=n:
8                ans=m
9                l=m+1
10            else:
11                h=m-1
12        return ans
13        
14        