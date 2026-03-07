# Last updated: 3/7/2026, 12:31:04 PM
# sliding window
1from collections import defaultdict
2class Solution:
3    def characterReplacement(self, s: str, k: int) -> int:
4        hashmap=defaultdict(int)
5        max_count=0
6        max_len=0
7        l=0
8        for r in range(len(s)):
9            hashmap[s[r]]+=1
10            max_count=max(max_count,hashmap[s[r]])
11            if r-l+1-max_count>k:
12                hashmap[s[l]]-=1
13                l+=1
14            max_len=max(max_len,r-l+1)
15
16        return max_len