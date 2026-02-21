# Last updated: 2/21/2026, 9:45:23 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)<=1:
            return strs[0]
        else:
            strs=sorted(strs,key=len)
            j=0
            while j< len(strs[0]):
                i=1
                flag=True
                while i<len(strs):
                    if strs[i][j]!=strs[0][j]:
                        flag=False
                        break
                    else:
                        i=i+1
                if flag==False:
                    return strs[0][:j]
                j=j+1
            return strs[0]
            
                    
                    
                
            