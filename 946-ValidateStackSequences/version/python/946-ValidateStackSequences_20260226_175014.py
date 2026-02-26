# Last updated: 2/26/2026, 5:50:14 PM
# append to stack and pop from popped
1class Solution:
2    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
3        stack=[]
4        n=len(pushed)
5        i=0
6        for val in pushed:
7            stack.append(val)
8            while stack and i<n and stack[-1]==popped[i]:
9                i+=1
10                stack.pop()
11        return len(stack)==0
12        