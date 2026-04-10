# Last updated: 4/10/2026, 7:01:56 PM
# topological sorting
1from collections import defaultdict,deque
2class Solution:
3    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
4        graph=defaultdict(list)
5        queue=deque()
6        indegrees=[0]*numCourses
7        for u,v in prerequisites:
8            graph[v].append(u)
9            indegrees[u]+=1
10        for i,degree in enumerate(indegrees):
11            if not degree:
12                queue.append(i)
13        while queue:
14            size=len(queue)
15            while size:
16                curr=queue.popleft()
17                for course in graph[curr]:
18                    indegrees[course]-=1
19                    if not indegrees[course]:
20                        queue.append(course)
21                size-=1
22        for degree in indegrees:
23            if degree:
24                return False
25        return True
26
27
28        