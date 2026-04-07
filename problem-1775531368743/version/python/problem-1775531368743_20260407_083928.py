# Last updated: 4/7/2026, 8:39:28 AM
# backtracking
1class Solution:
2    def wordSquares(self, words: List[str]) -> List[List[str]]:
3        results=[]
4        visited=[False]*len(words)
5        words.sort()
6        def backtrack(temp):
7            if len(temp)==4:
8                top,left,right,bottom=temp[0],temp[1],temp[2],temp[3]
9                if top[0]==left[0] and top[3]==right[0] and bottom[0]==left[3] and bottom[3]==right[3]:
10                    results.append(temp[:])
11                return
12            for i in range(len(words)):
13                if not visited[i]:
14                    visited[i]=True
15                    temp.append(words[i])
16                    backtrack(temp)
17                    temp.pop()
18                    visited[i]=False
19
20        backtrack([])
21        return results
22            