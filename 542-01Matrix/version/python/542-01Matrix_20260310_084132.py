# Last updated: 3/10/2026, 8:41:32 AM
# using deque added multiple sources and then did bfs
1from collections import deque
2class Solution:
3    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
4        queue=deque()
5        n,m=len(mat),len(mat[0])
6        for i in range(n):
7            for j in range(m):
8                if mat[i][j]==0:
9                    queue.append((i,j))
10                else:
11                    mat[i][j]=-1
12        directions=[[0,1],[0,-1],[1,0],[-1,0]]
13        while queue:
14            i,j=queue.popleft()
15            for dir in directions:
16                i_new=i+dir[0]
17                j_new=j+dir[1]
18                if i_new>=0 and i_new<n and j_new>=0 and j_new<m and mat[i_new][j_new]==-1:
19                    mat[i_new][j_new]=1+mat[i][j]
20                    queue.append((i_new,j_new))
21        return mat
22
23
24        