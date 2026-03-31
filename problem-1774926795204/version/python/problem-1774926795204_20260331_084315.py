# Last updated: 3/31/2026, 8:43:15 AM
# min_odd and min_even
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        min_odd,min_even=float('inf'),float('inf')
4        for num in nums1:
5            if num%2==1:
6                min_odd=min(min_odd,num)
7            else:
8                min_even=min(min_even,num)
9        if min_odd==float('inf') or min_even==float('inf'):
10            return True
11        if min_odd>min_even:
12            return False
13        else:
14            return True
15        