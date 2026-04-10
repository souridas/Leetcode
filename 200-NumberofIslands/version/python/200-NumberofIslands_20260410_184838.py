# Last updated: 4/10/2026, 6:48:38 PM
# simple dfs
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        n,m=len(grid),len(grid[0])
4        visited=set()
5        def dfs(i,j):
6            if i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0" or (i,j) in visited:
7                return
8            visited.add((i,j))
9            dfs(i,j+1)
10            dfs(i+1,j)
11            dfs(i,j-1)
12            dfs(i-1,j)
13        islands=0
14        for i in range(n):
15            for j in range(m):
16                if (i,j) not in visited and grid[i][j]=="1":
17                    dfs(i,j)
18                    islands+=1
19        return islands
20