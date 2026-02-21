# Last updated: 2/21/2026, 9:44:04 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_prod=[1]*n
        right_prod=[1]*n
        left_prod[0]=1

        for i in range(1,n,1):
                left_prod[i]=left_prod[i-1]*nums[i-1]

        right_prod[n-1]=1
        for i in range(n-2,-1,-1):
                right_prod[i]=right_prod[i+1]*nums[i+1]

        answer=[]
        for i in range(n):
            answer.append(right_prod[i]*left_prod[i])
        return answer