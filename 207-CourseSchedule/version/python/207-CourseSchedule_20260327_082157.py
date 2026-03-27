# Last updated: 3/27/2026, 8:21:57 AM
# topological sort revision
1from collections import defaultdict,deque
2class Solution:
3    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
4        queue=deque()
5        graph=defaultdict(list)
6        indegrees=defaultdict(int)
7        completed=0
8        for u,w in prerequisites:
9            indegrees[u]+=1
10            graph[w].append(u)
11        for i in range(numCourses):
12            if indegrees[i] == 0:
13                queue.append(i)
14        while queue:
15            curr_course=queue.popleft()
16            completed+=1
17            for prereq in graph[curr_course]:
18                indegrees[prereq]-=1
19                if not indegrees[prereq]:
20                    queue.append(prereq)
21        return completed==numCourses
22
23    