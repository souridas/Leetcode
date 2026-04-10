# Last updated: 4/10/2026, 6:32:46 PM
# bfs
1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        queue=deque()
5        visited=set()
6        time=-1
7        fresh_count=0
8        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
9        n,m=len(grid),len(grid[0])
10        for i in range(n):
11            for j in range(m):
12                if grid[i][j]==2:
13                        queue.append((i,j))
14                        visited.add((i,j)) 
15                elif grid[i][j]==1:
16                    fresh_count+=1
17        if not len(visited) and not fresh_count:
18            return 0
19        while queue:
20            size=len(queue)
21            time+=1
22            while size:
23                i,j=queue.popleft()
24                for d in dirs:
25                    i_new=i+d[0]
26                    j_new=j+d[1]
27                    if 0<=i_new<n and 0<=j_new<m and grid[i_new][j_new]==1 and (i_new,j_new) not in visited:
28                        visited.add((i_new,j_new))
29                        grid[i_new][j_new]=2
30                        queue.append((i_new,j_new))
31                        fresh_count-=1
32                size-=1
33        if fresh_count:
34            return -1
35        else:
36            return time
37
38
39