# Last updated: 2/25/2026, 8:16:03 AM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l,h=0,len(arr)-k
4        while l<h:
5            m=(l+h)//2
6            if x-arr[m]> arr[m+k]-x:
7                l=m+1
8            else:
9                h=m
10        return arr[l:l+k]