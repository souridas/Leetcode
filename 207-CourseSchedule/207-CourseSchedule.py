# Last updated: 2/21/2026, 9:44:13 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        queue=[]
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
        degrees=[0]*numCourses
        for i in range(numCourses):
            for node in adj[i]:
                degrees[node]+=1
        for i in range(numCourses):
            if degrees[i]==0:
                queue.append(i)
        while queue:
            top=queue.pop(0)
            for next_node in adj[top]:
                degrees[next_node]-=1
                if degrees[next_node]==0:
                    queue.append(next_node)
        for i in range(numCourses):
            if degrees[i]!=0:
                return False
        return True

        