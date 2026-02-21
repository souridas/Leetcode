# Last updated: 2/21/2026, 9:44:34 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        ans.append([1])
        ans.append([1,1])
        for i in range(2,numRows):
            curr=[]
            curr.append(1)
            prev=ans[-1]
            for i in range(len(prev)-1):
                curr.append(prev[i]+prev[i+1])
            curr.append(1)
            ans.append(curr)
        return ans