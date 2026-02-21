# Last updated: 2/21/2026, 9:44:54 AM
def binary_func(x,l,h):
    ans=0
    while l<=h:
        m=(l+h)//2
        if m*m==x:
            return m
        elif m*m<x:
            ans=m
            l=m+1
        else:
            h=m-1
    return ans
class Solution:
    def mySqrt(self, x: int) -> int:
        return binary_func(x,0,x)
        