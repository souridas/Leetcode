# Last updated: 3/11/2026, 12:21:55 PM
1import heapq
2class Solution:
3    def minimumEffortPath(self, heights: List[List[int]]) -> int:
4        n,m=len(heights),len(heights[0])
5        min_efforts=[[float('inf')]*m for _ in range(n)]
6        min_efforts[0][0]=0
7        min_heap=[(0,0,0)]
8        directions=[[0,1],[0,-1],[1,0],[-1,0]]
9        while min_heap:
10            h,r,c=heapq.heappop(min_heap)
11            if r==n-1 and c==m-1:
12                return min_efforts[r][c]
13            if h>min_efforts[r][c]:
14                continue
15            for dir in directions:
16                r_new=r+dir[0]
17                c_new=c+dir[1]
18                if r_new>=0 and c_new>=0 and r_new<n and c_new<m:
19                    distance_temp= max(h,abs(heights[r_new][c_new]-heights[r][c]))  
20                    if distance_temp<min_efforts[r_new][c_new]:
21                        min_efforts[r_new][c_new]=distance_temp
22                        heapq.heappush(min_heap,(distance_temp,r_new,c_new))
23        return 0
24        