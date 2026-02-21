# Last updated: 2/21/2026, 9:44:44 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def dfs(i,nums,temp):
            if i==len(nums) :
                result.append(temp[:])
                return
            dfs(i+1,nums,temp)
            temp.append(nums[i])
            dfs(i+1,nums,temp)
            temp.pop()
        dfs(0,nums,[])
        final=[]
        for i in range(len(result)):
            flag=0
            for j in range(i+1,len(result)):
                if result[i]==result[j]:
                    flag=1
                    break
            if flag==0:
                    final.append(result[i])
        return final
                
                    
        