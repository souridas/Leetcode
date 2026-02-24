# Last updated: 2/24/2026, 11:24:30 AM
# using 2 pointers, if both the characters are same increment both by 1, elif previous element in typed is same increment j, else return False. then handl;e the case where loop ends
1class Solution:
2    def isLongPressedName(self, name: str, typed: str) -> bool:
3        i=0
4        j=0
5        n=len(name)
6        m=len(typed)
7        while i<n and j<m:
8            if name[i]==typed[j]:
9                    j+=1
10                    i+=1
11            elif j>0  and typed[j]==typed[j-1]:
12                    j+=1
13            else:
14                return False
15            
16        if i!=n:
17            return False
18        else:
19            while j<m:
20                if typed[j]!=typed[j-1]:
21                    return False
22                j+=1
23        return True
24
25        