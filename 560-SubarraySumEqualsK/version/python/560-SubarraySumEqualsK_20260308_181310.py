# Last updated: 3/8/2026, 6:13:10 PM
# On(n) solution use the idea that sum(i)-sum(j)=k
1from collections import defaultdict
2class Solution:
3    def subarraySum(self, nums: List[int], k: int) -> int:
4        hashmap=defaultdict(int)
5        sum=0
6        count=0
7        hashmap[0]=1
8        for num in nums:
9            sum+=num
10            if sum-k in hashmap:
11                count+=hashmap[sum-k]
12            hashmap[sum]+=1
13        return count
14
15        