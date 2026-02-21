# Last updated: 2/21/2026, 9:44:18 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        visited = [[False]*n for _ in range(m)]
        islands=0
        def BFS(node,queue):
            i=node[0]
            j=node[1]
            queue.append(node)
            visited[i][j]=True
            flag=0
            while queue:
                curr=queue.pop(0)
                curr_x=curr[0]
                curr_y=curr[1]
                if curr_x>0 and not visited[curr_x-1][curr_y] and grid[curr_x-1][curr_y]=="1":
                    queue.append([curr_x-1,curr_y])
                    visited[curr_x-1][curr_y]=True
                if curr_x<m-1 and not visited[curr_x+1][curr_y] and grid[curr_x+1][curr_y]=="1":
                    queue.append([curr_x+1,curr_y])
                    visited[curr_x+1][curr_y]=True
                if curr_y>0 and not visited[curr_x][curr_y-1] and grid[curr_x][curr_y-1]=="1":
                    queue.append([curr_x,curr_y-1])
                    visited[curr_x][curr_y-1]=True
                if curr_y<n-1 and not visited[curr_x][curr_y+1] and grid[curr_x][curr_y+1]=="1":
                    queue.append([curr_x,curr_y+1])
                    visited[curr_x][curr_y+1]=True
                flag=1
            return flag
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    cnt = BFS([i,j],[])
                    islands+=cnt
        return islands

        