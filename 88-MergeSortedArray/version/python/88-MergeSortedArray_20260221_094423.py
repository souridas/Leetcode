# Last updated: 2/21/2026, 9:44:23 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i=0
7        j=0
8        k=m
9        while i<(n+m)-1 and j<n and k<(n+m):
10
11            if nums2[j]<=nums1[i]:
12                for l in range(k,i-1,-1):
13                    nums1[l]=nums1[l-1]
14                nums1[i]=nums2[j]
15                j+=1
16                k+=1
17            else:
18                i+=1
19        while k<(n+m) and j<n:
20            nums1[k]=nums2[j]
21            k+=1
22            j+=1
23        return
24
25
26        