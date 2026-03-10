# Last updated: 3/10/2026, 9:12:07 AM
# find the no of levels basically using multisource bfs traversal
1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        queue=deque()
5        time=0
6        fresh_count=0
7        n,m=len(grid),len(grid[0])
8        for i in range(n):
9            for j in range(m):
10                if grid[i][j]==2:
11                    queue.append((i,j))
12                elif grid[i][j]==1:
13                    fresh_count+=1
14        if fresh_count==0:
15            return 0
16        directions=[[0,1],[0,-1],[1,0],[-1,0]]
17        while queue:
18            neighbours=len(queue)
19            for nbr in range(neighbours):
20                i,j=queue.popleft()
21                for dir in directions:
22                    i_new=i+dir[0]
23                    j_new=j+dir[1]
24                    if i_new>=0 and j_new>=0 and i_new<n and j_new<m and grid[i_new][j_new]==1:
25                        grid[i_new][j_new]=2
26                        fresh_count-=1
27                        queue.append((i_new,j_new))
28            if queue:
29                time+=1
30        if fresh_count: 
31            return -1 
32        else: 
33            return time
34
35        