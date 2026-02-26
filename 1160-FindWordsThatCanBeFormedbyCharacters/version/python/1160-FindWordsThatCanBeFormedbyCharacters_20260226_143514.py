# Last updated: 2/26/2026, 2:35:14 PM
# hashmap
1from collections import defaultdict
2class Solution:
3    def countCharacters(self, words: List[str], chars: str) -> int:
4        target_map=defaultdict(int)
5        for c in chars:
6            target_map[c]+=1
7        ans=0
8        for word in words:
9            temp_target=target_map.copy()
10            flag=0
11            for c in word:
12                if c in temp_target and temp_target[c]>0:
13                    temp_target[c]-=1
14                else:
15                    flag=1
16                    break
17            if flag==0:
18                ans+=len(word)
19        return ans
20        