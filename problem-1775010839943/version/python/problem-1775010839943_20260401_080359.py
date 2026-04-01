# Last updated: 4/1/2026, 8:03:59 AM
# simple loop
1class Solution:
2    def trimTrailingVowels(self, s: str) -> str:
3        i=len(s)-1
4        while i>=0 and s[i] in ['a','e','i','o','u']:
5            i-=1
6        return s[:i+1]
7        
8            
9        