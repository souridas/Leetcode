# Last updated: 3/27/2026, 8:37:12 AM
# revisiting djiskstras
1from collections import defaultdict
2import heapq
3class Solution:
4    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
5        graph=defaultdict(list)
6        for u,v,w in times:
7            graph[u].append((v,w))
8        distances={i:float('inf') for i in range(1,n+1)}
9        distances[k]=0
10        min_heap=[(0,k)]
11        while min_heap:
12            curr_distance,curr_node=heapq.heappop(min_heap)
13            if curr_distance>distances[curr_node]:
14                continue
15            for v,w in graph[curr_node]:
16                new_distance=curr_distance+w
17                if new_distance<distances[v]:
18                    distances[v]=new_distance
19                    heapq.heappush(min_heap,(new_distance,v))
20        if max(distances.values())==float('inf'):
21            return -1
22        return max(distances.values())
23