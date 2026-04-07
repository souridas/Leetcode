# Last updated: 4/7/2026, 8:11:44 AM
# iterate from left
1class Solution:
2    def largestEven(self, s: str) -> str:
3        i=len(s)-1
4        if s[i]=='2':
5            return s
6        while i>=0 and s[i]=='1':
7            i-=1
8        return s[:i+1]