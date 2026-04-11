# Last updated: 4/11/2026, 10:59:42 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        brackets=[]
4        asterisks=[]
5        for i,c in enumerate(s):
6            if c=="(":
7                brackets.append(i)
8            elif c=="*":
9                asterisks.append(i)
10            else:
11                if brackets:
12                    brackets.pop()
13                elif asterisks:
14                    asterisks.pop()
15                else:
16                    return False
17        while brackets and asterisks:
18            if brackets.pop()>asterisks.pop():
19                return False
20        return not brackets
21
22        
23            
24
25        