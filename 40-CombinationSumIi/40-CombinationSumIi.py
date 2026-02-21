# Last updated: 2/21/2026, 9:45:08 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def dfs(i,candidates,target,temp):
            if sum(temp)==target:
                    result.append(temp[:])
                    return
            for j in range(i,len(candidates)):
                if i!=j and candidates[j]==candidates[j-1]:
                    continue
                if  sum(temp)+candidates[j] <= target:
                    temp.append(candidates[j])
                    dfs(j+1,candidates,target,temp)
                    temp.pop()
        dfs(0,candidates,target,[])
        return result