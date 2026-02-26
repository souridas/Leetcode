# Last updated: 2/26/2026, 9:28:06 AM
# simple hashmap
1from collections import defaultdict
2class Solution:
3    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
4        hash_map=defaultdict(int)
5        for word in s1.split(' '):
6            hash_map[word]+=1
7        for word in s2.split(' '):
8            hash_map[word]+=1
9        ans=[]
10        for k,v in hash_map.items():
11            if v==1:
12                ans.append(k)
13        return ans