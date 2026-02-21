# Last updated: 2/21/2026, 9:43:47 AM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        store={}
        odd_flag=0
        for c in s:
            if c not in store:
                store[c]=1
            else:
                store[c]+=1
        answer=0
        for k,v in store.items():
            if v%2==1:
                answer+=v-1
                odd_flag=1
            elif v%2==0:
                answer+=v
        return answer + odd_flag
        