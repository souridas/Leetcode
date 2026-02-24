# Last updated: 2/24/2026, 12:00:00 PM
# sliding window hashmap
1from collections import defaultdict
2class Solution:
3    def totalFruit(self, fruits: List[int]) -> int:
4        left,right=0,0
5        fruit_store=defaultdict(int)
6        ans=0
7        for right,fruit in enumerate(fruits):
8            fruit_store[fruit]+=1
9            while len(fruit_store)>2:
10                fruit_store[fruits[left]]-=1
11                if not fruit_store[fruits[left]]:
12                    del fruit_store[fruits[left]]
13                left+=1
14            ans=max(ans,right-left+1)
15        return ans
16       
17                
18
19        