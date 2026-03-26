# Last updated: 3/26/2026, 10:07:48 PM
# dfs
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        n,m=len(grid),len(grid[0])
4        visited=[]
5        def dfs(i,j):
6            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0 or (i,j) in visited:
7                return 0
8            visited.append((i,j))
9            return 1+ dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
10        ans=0
11        for i in range(n):
12            for j in range(m):
13                if grid[i][j]==1 and (i,j) not in visited:
14                    area=dfs(i,j)
15                    ans=max(ans,area)
16                else:
17                    continue
18        return ans
19
20