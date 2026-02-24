# Last updated: 2/24/2026, 10:09:42 AM
# base = max(end,base+1) and then just loops
1class Solution:
2    def longestMountain(self, arr: List[int]) -> int:
3        n=len(arr)
4        base=0
5        result=0
6        while base<n:
7            end=base
8            if end+1<n and arr[end]<arr[end+1]:
9                while end+1<n and arr[end]<arr[end+1]:
10                    end+=1
11                if end+1<n and arr[end]>arr[end+1]:
12                    while end+1<n and arr[end]>arr[end+1]:
13                        end+=1
14                    result = max(result,end-base+1)
15            base = max(end,base+1)     
16        return result   