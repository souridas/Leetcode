# Last updated: 3/7/2026, 4:58:33 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        result=[]
4        def dfs(temp,i):
5            if i>=len(nums):
6                result.append(temp.copy())
7                return
8            temp.append(nums[i])
9            dfs(temp,i+1)
10            temp.pop()
11            dfs(temp,i+1)
12        dfs([],0)
13        return result