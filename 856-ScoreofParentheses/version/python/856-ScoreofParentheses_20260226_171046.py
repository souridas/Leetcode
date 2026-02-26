# Last updated: 2/26/2026, 5:10:46 PM
# reomove () but keep the outer (
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        stack=[]
4        ans=0
5        flag=0
6        for c in s:
7            if c=='(':
8                flag=1
9                stack.append('(')
10            if c==')':
11                if flag==1:
12                    ans+=2**(len(stack)-1)
13                    flag=0
14                stack.pop()
15                
16        return ans
17    
18
19        