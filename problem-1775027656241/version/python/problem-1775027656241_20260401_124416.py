# Last updated: 4/1/2026, 12:44:16 PM
# dictionary use
1class Solution:
2    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
3        store={}
4        for num in nums:
5            if num not in store:
6                store[num]=0
7            else:
8                store[num]+=1
9        sorted_dict=dict(sorted(store.items()))
10        for k1,v1 in sorted_dict.items():
11            for k2,v2 in sorted_dict.items():
12                if k1!=k2 and v1!=v2:
13                    return [k1,k2]
14        return [-1,-1]
15            
16            
17        