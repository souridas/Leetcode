# Last updated: 3/30/2026, 8:54:11 AM
# 2 pointers
1class Solution:
2    def firstMatchingIndex(self, s: str) -> int:
3        l,r=0,len(s)-1
4        while l<=r:
5            if s[l]==s[r]:
6                return l
7            l+=1
8            r-=1
9        return -1