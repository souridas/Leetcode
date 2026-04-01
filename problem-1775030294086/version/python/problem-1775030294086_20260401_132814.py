# Last updated: 4/1/2026, 1:28:14 PM
# array problem
1class Solution:
2    def mergeCharacters(self, s: str, k: int) -> str:
3        temp=[]
4        for i in range(len(s)):
5            curr=s[i]
6            flag=0
7            for j in range(max(0,len(temp)-k),len(temp)):
8                if curr==temp[j]:
9                    flag=1
10                    break
11            if flag==0:
12                temp.append(curr)
13        return "".join(temp)
14                
15            
16        