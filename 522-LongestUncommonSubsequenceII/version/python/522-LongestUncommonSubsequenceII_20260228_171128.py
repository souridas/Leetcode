# Last updated: 2/28/2026, 5:11:28 PM
1class Solution:
2    def findLUSlength(self, strs: List[str]) -> int:
3        def check_subsequence(w1,w2):
4            i=0
5            for c in w2:
6                if i<len(w1) and w1[i]==c:
7                    i+=1
8            return i==len(w1)
9        strs.sort(key=len,reverse=True)
10        for i,w1 in enumerate(strs):
11            if  all(not check_subsequence(w1,w2) for j,w2 in enumerate(strs) if i!=j):
12                return len(w1)
13        return -1
14
15        