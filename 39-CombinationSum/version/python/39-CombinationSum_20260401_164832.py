# Last updated: 4/1/2026, 4:48:32 PM
# simple backtrack
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        results=[]
4        def backtrack(idx,temp,curr_sum):
5            if curr_sum==target:
6                results.append(temp[:])
7            for i in range(idx,len(candidates)):
8                if curr_sum+candidates[i]<=target:
9                    temp.append(candidates[i])
10                    backtrack(i,temp,curr_sum+candidates[i])
11                    temp.pop()
12        backtrack(0,[],0)
13        return results
14            