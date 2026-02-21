# Last updated: 2/21/2026, 9:43:20 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=list([0]*n)
        h=n-1
        l=0
        i=n-1
        while l<=h and i>=0:
            if abs(nums[l])<= abs(nums[h]):
                answer[i]=nums[h]*nums[h]
                h-=1
            else:
                answer[i]=nums[l]*nums[l]
                l+=1
            i-=1
        return answer
