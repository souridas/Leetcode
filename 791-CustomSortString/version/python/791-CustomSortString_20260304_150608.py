# Last updated: 3/4/2026, 3:06:08 PM
# hashmap
1from collections import defaultdict
2class Solution:
3    def customSortString(self, order: str, s: str) -> str:
4        hashmap=defaultdict(int)
5        ans=""
6        for c in s:
7            hashmap[c]+=1
8        for c in order:
9            if c in hashmap:
10                while hashmap[c]:
11                    ans+=c
12                    hashmap[c]-=1
13                if hashmap[c]==0:
14                    del hashmap[c]
15        for c in hashmap:
16            while hashmap[c]:
17                ans+=c
18                hashmap[c]-=1
19        return ans             
20        