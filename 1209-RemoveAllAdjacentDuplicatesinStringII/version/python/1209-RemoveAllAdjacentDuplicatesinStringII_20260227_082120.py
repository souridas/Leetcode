# Last updated: 2/27/2026, 8:21:20 AM
# stack of lsit (with key,value pair)
1class Solution:
2    def removeDuplicates(self, s: str, k: int) -> str:
3        stack=[]
4        for c in s:
5            if stack and stack[-1][0]==c:
6                stack[-1][1]+=1
7                if stack[-1][1]==k:
8                    stack.pop()
9            else:
10                stack.append([c,1])
11        return "".join(c*cnt for c,cnt in stack)
12