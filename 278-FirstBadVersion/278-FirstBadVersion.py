# Last updated: 2/21/2026, 9:43:57 AM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        i=1
        j=n
        while(i<=j):
            m=(i+j)//2
            if isBadVersion(m) and not isBadVersion(m-1):
                return m

            if not isBadVersion(m):
                i=m+1
            else:
                j=m-1
        return -1 
        