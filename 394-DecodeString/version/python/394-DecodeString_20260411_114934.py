# Last updated: 4/11/2026, 11:49:34 AM
# stack append current string and number
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack=[]
4        curr_num=0
5        curr_str=""
6        for c in s:
7            if c.isdigit():
8                curr_num=curr_num*10+int(c)
9            elif c=="[":
10                stack.append((curr_str,curr_num))
11                curr_str=""
12                curr_num=0
13            elif c=="]":
14                last_str,num=stack.pop()
15                curr_str=last_str+curr_str*num
16            else:
17                curr_str+=c
18        return curr_str
19
20        