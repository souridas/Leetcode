# Last updated: 2/21/2026, 9:44:30 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        store=[]
        for c in s:
            if c.isalnum():
                store.append(c.lower())
        i=0
        j=len(store)-1
        while (i<=j):
            if store[i]!=store[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        