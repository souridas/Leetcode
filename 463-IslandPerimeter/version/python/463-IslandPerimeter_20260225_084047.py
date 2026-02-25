# Last updated: 2/25/2026, 8:40:47 AM
# hashmap of sides
1from collections import defaultdict
2class Solution:
3    def islandPerimeter(self, grid: List[List[int]]) -> int:
4        square=defaultdict(int)
5        for i in range(len(grid)):
6            for j in range(len(grid[0])):
7                if grid[i][j]==1:
8                    square[0]+=1
9                    square[1]+=1
10                    square[2]+=1
11                    square[3]+=1
12                    if i>0 and grid[i-1][j]==1:
13                        square[0]-=1
14                    if j>0 and grid[i][j-1]==1:
15                        square[3]-=1
16                    if i<len(grid)-1 and grid[i+1][j]==1:
17                        square[2]-=1
18                    if j<len(grid[0])-1 and grid[i][j+1]==1:
19                        square[1]-=1
20        perimeter=0
21        for key in square:
22            if square[key]:
23                perimeter+=square[key]
24        return perimeter
25
26
27        