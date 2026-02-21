# Last updated: 2/21/2026, 9:45:29 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j=0
        n=len(s)
        max_len=0
        while j<n:
            store={}
            local_len=0
            while j<n:
                if s[j] not in store:
                    store[s[j]]=j
                    j+=1
                    local_len+=1
                else:
                    j=store[s[j]]+1
                    break
            max_len = max(max_len,local_len)
        return max_len
