# Last updated: 3/12/2026, 9:25:21 AM
# floyd marshall
1class Solution:
2    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
3        distances=[[float('inf')]*n for _ in range(n)]
4        for i in range(n):
5            distances[i][i]=0
6        for u,v,w in edges:
7            distances[u][v]=w
8            distances[v][u]=w
9        for k in range(n):
10            for i in range(n):
11                for j in range(n):
12                    if distances[i][j]>distances[i][k]+distances[k][j]:
13                        distances[i][j]=distances[i][k]+distances[k][j]
14        ans=-1
15        min_cities=float('inf')
16        for i in range(n):
17            count=0
18            for j in range(n):
19                if i!=j and distances[i][j]<=distanceThreshold:
20                    count+=1
21            if count<=min_cities:
22                ans=i
23                min_cities=count
24        return ans
25