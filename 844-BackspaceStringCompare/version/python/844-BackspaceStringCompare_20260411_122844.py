# Last updated: 4/11/2026, 12:28:44 PM
# stack
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        stack1,stack2=[],[]
4        for c in s:
5            if c!="#":
6                stack1.append(c)
7            else:
8                if stack1:
9                    stack1.pop()
10        for c in t:
11            if c!="#":
12                stack2.append(c)
13            else:
14                if stack2:
15                    stack2.pop()
16        return "".join(stack1)=="".join(stack2)
17
18        