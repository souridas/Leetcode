# Last updated: 2/21/2026, 9:45:10 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def dfs(i,candidates,target,temp):
            if sum(temp)==target:
                    result.append(temp[:])
                    return

            for j in range(i,len(candidates)):
                val=candidates[j]
                if sum(temp)+val<=target:
                    temp.append(val)
                    dfs(j,candidates,target,temp)
                    temp.pop()
                else:
                    continue
        dfs(0,candidates,target,[])

        return result
