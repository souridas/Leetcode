# Last updated: 2/24/2026, 7:40:56 PM
1def binary_func(x,l,h):
2    ans=0
3    while l<=h:
4        m=(l+h)//2
5        if m*m==x:
6            return m
7        elif m*m<x:
8            ans=m
9            l=m+1
10        else:
11            h=m-1
12    return ans
13class Solution:
14    def mySqrt(self, x: int) -> int:
15        return binary_func(x,0,x)
16        