# Last updated: 2/24/2026, 7:42:03 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        l,h=0,x
4        while l<=h:
5            m= (l+h)//2
6            if m*m>x:
7                h=m-1
8            elif m*m<x:
9                l=m+1
10            else:
11                return m
12        if m*m>x:
13            return m-1
14        else:
15            return m
16        