# Last updated: 2/21/2026, 9:44:45 AM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        k=m
        while i<(n+m) and j<n and k<(n+m):

            if nums2[j]<=nums1[i]:
                for l in range(k,i-1,-1):
                    nums1[l]=nums1[l-1]
                nums1[i]=nums2[j]
                j+=1
                k+=1
            else:
                i+=1
        while k<(n+m) and j<n:
            nums1[k]=nums2[j]
            k+=1
            j+=1
        return


        