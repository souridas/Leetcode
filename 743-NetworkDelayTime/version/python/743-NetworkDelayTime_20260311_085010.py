# Last updated: 3/11/2026, 8:50:10 AM
# using heapq
1import heapq
2from collections import defaultdict
3class Solution:
4    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
5        graph=defaultdict(list)
6        for u,v,w in times:
7            graph[u].append((v,w))
8        min_heap=[(0,k)]
9        distance={i:float('inf') for i in range(1,n+1)}
10        distance[k]=0
11        while min_heap:
12            curr_distance,u=heapq.heappop(min_heap)
13            if curr_distance>distance[u]:
14                continue
15            for neighbour,w in graph[u]:
16                distance_temp=w+curr_distance
17                if distance_temp<distance[neighbour]:
18                    distance[neighbour]=distance_temp
19                    heapq.heappush(min_heap,(distance_temp,neighbour))
20        max_time=max(distance.values())
21        if max_time<float('inf'):
22            return max_time
23        else:
24            return -1
25
26                
27        