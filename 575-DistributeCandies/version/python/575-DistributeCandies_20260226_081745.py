# Last updated: 2/26/2026, 8:17:45 AM
# hashmap
1from collections import defaultdict
2class Solution:
3    def distributeCandies(self, candyType: List[int]) -> int:
4        hash_map=defaultdict(int)
5        n=len(candyType)
6        for candy in candyType:
7            hash_map[candy]+=1
8        return min(n//2,len(hash_map))
9
10        