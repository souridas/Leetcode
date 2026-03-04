# Last updated: 3/4/2026, 9:16:53 AM
1from collections import defaultdict
2class Solution:
3    def totalFruit(self, fruits: List[int]) -> int:
4        hashmap=defaultdict(int)
5        l=0
6        ans=0
7        for r,fruit in enumerate(fruits):
8            hashmap[fruit]+=1
9            while len(hashmap)>2:
10                hashmap[fruits[l]]-=1
11                if hashmap[fruits[l]]==0:
12                    del hashmap[fruits[l]]
13                l+=1
14            if len(hashmap)<=2:
15                ans=max(ans,r-l+1)
16        return ans
17