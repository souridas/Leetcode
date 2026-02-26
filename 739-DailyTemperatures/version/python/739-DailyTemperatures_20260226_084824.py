# Last updated: 2/26/2026, 8:48:24 AM
# next greatest elenent using stack
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        n=len(temperatures)
4        result=[0]*n
5        stack=[]
6        for i,temp in enumerate(temperatures):
7            while stack and temperatures[stack[-1]]<temp:
8                idx=stack.pop()
9                result[idx]=i-idx
10            stack.append(i)
11        return result
12        