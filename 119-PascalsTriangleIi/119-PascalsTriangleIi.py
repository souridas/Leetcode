# Last updated: 2/21/2026, 9:44:33 AM
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        ans.append(1)
       
        for i in range(rowIndex):
            ans.append(ans[-1]*(rowIndex-i)//(i+1))
        return ans
            