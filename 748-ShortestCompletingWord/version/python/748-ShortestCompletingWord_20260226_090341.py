# Last updated: 2/26/2026, 9:03:41 AM
# simple hashmap
1from collections import defaultdict
2class Solution:
3    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
4        license_map=defaultdict(int)
5        min_len=1e6
6        for c in licensePlate:
7            if c.isalpha():
8                license_map[c.lower()]+=1
9        for word in words:
10            temp_map=defaultdict(int)
11            for c in word:
12                if c.isalpha():
13                    temp_map[c.lower()]+=1
14            flag=0
15            for c in license_map:
16                if c not in temp_map:
17                    flag=1
18                    break
19                else:
20                    if license_map[c]>temp_map[c]:
21                        flag=1
22                        break
23            if flag==0:
24                if len(word)<min_len:
25                    ans=word
26                    min_len=len(word)
27        return ans
28
29