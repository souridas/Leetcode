# Last updated: 3/10/2026, 8:20:26 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5        n,m=len(grid),len(grid[0])
6        total_islands=0
7        visited=set()
8        def dfs(i,j):
9            if i>=n or i<0 or j>=m or j<0 or grid[i][j]=='0' or (i,j) in visited:
10                return
11            visited.add((i,j))
12            dfs(i+1,j)
13            dfs(i-1,j)
14            dfs(i,j+1)
15            dfs(i,j-1)
16        for i in range(n):
17            for j in range(m):
18                if grid[i][j]=='1' and (i,j) not in visited:
19                    dfs(i,j)
20                    total_islands+=1
21        return total_islands
22            