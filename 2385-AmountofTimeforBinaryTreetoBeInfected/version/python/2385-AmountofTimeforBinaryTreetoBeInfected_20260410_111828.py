# Last updated: 4/10/2026, 11:18:28 AM
# bfs
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import defaultdict,deque
8class Solution:
9    def __init__(self):
10        self.graph=defaultdict(list)
11        self.queue=deque()
12        self.visited=set()
13    def create_graph(self,node):
14        if not node:
15            return
16        if node.left:
17            self.graph[node.left.val].append(node.val)
18            self.graph[node.val].append(node.left.val)
19        if node.right:
20            self.graph[node.right.val].append(node.val)
21            self.graph[node.val].append(node.right.val)
22        self.create_graph(node.left)
23        self.create_graph(node.right)
24    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
25        self.create_graph(root)
26        time=0
27        self.queue.append(start)
28        self.visited.add(start)
29        while self.queue:
30            level_size=len(self.queue)
31            while level_size:
32                curr=self.queue.popleft()
33                for node in self.graph[curr]:
34                    if node not in self.visited:
35                        self.visited.add(node)
36                        self.queue.append(node)
37                level_size-=1
38            time+=1
39        return time-1
40
41
42
43        
44
45
46        