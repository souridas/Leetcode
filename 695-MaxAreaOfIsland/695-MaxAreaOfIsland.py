# Last updated: 2/21/2026, 9:43:33 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)-1
        n=len(grid[0])-1
        seen=set()
        answer=0
        def dfs(x,y):
            if x<0 or y<0 or x>m or y>n or grid[x][y]==0 or (x,y) in seen:
                return 0
            seen.add((x,y))
            return 1+dfs(x+1,y)+dfs(x-1,y)+dfs(x,y+1)+dfs(x,y-1)
        for i in range(m+1):
            for j in range(n+1):
                if grid[i][j]==1:
                    answer=max(answer,dfs(i,j))
        return answer
            