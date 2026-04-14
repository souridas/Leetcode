# Last updated: 4/14/2026, 9:42:01 AM
# max([0:n-1],[1:])
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        def max_money(houses):
7            prev_1=0
8            prev_2=0
9            curr=0
10            for money in houses:
11                curr=max(prev_1,prev_2+money)
12                prev_2=prev_1
13                prev_1=curr
14            return curr
15        m1=max_money(nums[:n-1])
16        m2=max_money(nums[1:])
17        return max(m1,m2)
18        