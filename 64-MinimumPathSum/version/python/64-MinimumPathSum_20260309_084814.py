# Last updated: 3/9/2026, 8:48:14 AM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        n,m=len(grid),len(grid[0])
4        for i in range(1,n):
5            grid[i][0]+=grid[i-1][0]
6        for j in range(1,m):
7            grid[0][j]+=grid[0][j-1]
8        for i in range(1,n):
9            for j in range(1,m):
10                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
11        return  grid[n-1][m-1]       