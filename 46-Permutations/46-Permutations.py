# Last updated: 2/21/2026, 9:45:07 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(nums,temp,visited):
            if len(temp)==len(nums):
                result.append(temp[:])
                return
            for j in range(len(nums)):
                if not visited[j]:
                    temp.append(nums[j])
                    visited[j]=1
                    dfs(nums,temp,visited)
                    visited[j]=0
                    temp.pop()
        visited=[0]*len(nums)      
        dfs(nums,[],visited)
        return result