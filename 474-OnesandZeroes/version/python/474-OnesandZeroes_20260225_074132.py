# Last updated: 2/25/2026, 7:41:32 AM
1class Solution:
2    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
3        houses.sort()
4        heaters.sort()
5        ans=0
6        for house in houses:
7            l,h=0,len(heaters)-1
8            pos=h
9            while l<=h:
10                m=(l+h)//2
11                if heaters[m]>=house:
12                    pos=m
13                    h=m-1
14                else:
15                    l=m+1
16            dist=abs(heaters[pos]-house)
17            if pos>0:
18                dist = min(dist, abs(heaters[pos-1]-house))
19            ans=max(ans,dist)
20        return ans
21            
22        