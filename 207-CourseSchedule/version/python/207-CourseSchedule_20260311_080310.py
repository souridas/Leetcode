# Last updated: 3/11/2026, 8:03:10 AM
1from collections import defaultdict,deque
2class Solution:
3    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
4        queue=deque()
5        graph=defaultdict(list)
6        degrees=defaultdict(int)
7        for course,prereq in prerequisites:
8            graph[prereq].append(course)
9            degrees[course]+=1
10        for course in range(numCourses):
11            if degrees[course]==0:
12                queue.append(course)
13        completed_courses=0
14        while queue:
15            prereq=queue.popleft()
16            completed_courses+=1
17            for course in graph[prereq]:
18                degrees[course]-=1
19                if degrees[course]==0:
20                    queue.append(course)
21        return completed_courses==numCourses
22        