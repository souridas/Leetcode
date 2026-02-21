# Last updated: 2/21/2026, 9:44:12 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        answer=[]
        for course,prereq in prerequisites:
            graph[prereq].append(course)

        indegrees= [0]*numCourses
        for course,_ in prerequisites:
            indegrees[course]+=1
        
        queue=deque()
        for course in range(numCourses):
            if indegrees[course]==0:
                answer.append(course)
                queue.append(course)
            
        while queue:
            prereq=queue.popleft()
            for course in graph[prereq]:
                indegrees[course]-=1
                if indegrees[course]==0:
                    answer.append(course)
                    queue.append(course)
        
        for v in indegrees:
            if v!=0:
                return []
        return answer
