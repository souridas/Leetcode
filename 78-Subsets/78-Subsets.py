# Last updated: 2/21/2026, 9:44:49 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(i,nums,temp):
            if i==len(nums):
                result.append(temp[:])
                return
            #exclude case
            dfs(i+1,nums,temp)
            #include case
            temp.append(nums[i])
            dfs(i+1,nums,temp)
            temp.pop()
        dfs(0,nums,[])
        return result