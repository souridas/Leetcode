# Last updated: 2/21/2026, 9:43:49 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store={}
        for c in magazine:
            if c not in store:
                store[c]=1
            else:
                store[c]+=1
        for c in ransomNote:
            if c not in store:
                return False
            if c in store:
                store[c]-=1
                if store[c]<0:
                    return False
        return True
        