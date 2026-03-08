# Last updated: 3/8/2026, 8:49:41 AM
# check if sum(array)//2 is attainable
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        target=sum(nums)//2
4        if sum(nums)%2!=0:
5            return False
6        store=[False]*(target+1)
7        store[0]=True
8        for num in nums:
9            for i in range(target,num-1,-1):
10                store[i]=store[i]or store[i-num]
11        return store[target]
12        
13        