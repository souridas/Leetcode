# Last updated: 2/21/2026, 9:45:13 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        else:
            i=0
            
            while i<len(haystack):
                if haystack[i]==needle[0]:
                    j=0
                    k=i
                    while k<len(haystack) and j<len(needle) and haystack[k]==needle[j]:
                        j=j+1
                        k=k+1
                    if k-i == len(needle):
                        return i
                i=i+1
            return -1