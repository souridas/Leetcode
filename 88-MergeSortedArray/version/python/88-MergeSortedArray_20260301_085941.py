# Last updated: 3/1/2026, 8:59:41 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i=m-1
7        j=n-1
8        k=m+n-1
9        while i>=0 and j>=0:
10            if nums1[i]>nums2[j]:
11                nums1[k]=nums1[i]
12                i-=1
13                k-=1
14            else:
15                nums1[k]=nums2[j]
16                j-=1
17                k-=1
18        while j>=0:
19            nums1[k]=nums2[j]
20            k-=1
21            j-=1
22        return
23
24
25        