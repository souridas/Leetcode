# Last updated: 2/21/2026, 9:43:28 AM
class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:
        result=[]

        def dfs(i,s,temp):
            if i == len(s):
                if temp not in result:
                    result.append(temp[:])
                return
            if  s[i].isalpha():
                #smaller case
                temp+=s[i].lower()
                dfs(i+1,s,temp)
                temp=temp[:-1]
                #upper case
                temp+=s[i].upper()
                dfs(i+1,s,temp)
                temp=temp[:-1]
            else:
                temp+=s[i]
                dfs(i+1,s,temp)
                temp=temp[:-1]

        dfs(0,s,"")
        return result




        