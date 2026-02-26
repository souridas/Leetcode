# Last updated: 2/26/2026, 3:12:40 PM
# stack
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        stack=[]
4        ans=0
5        for op in operations:
6            if op not in ["+","C","D"]:
7                stack.append(int(op))
8            elif op=="C":
9                stack.pop()
10            elif op=="D":
11                stack.append(2*stack[-1])
12            else:
13                stack.append(stack[-1]+stack[-2])
14        while stack:
15            ans+=stack.pop()
16        return ans