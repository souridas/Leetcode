# Last updated: 3/4/2026, 2:29:51 PM
# sort array of minutes, handle the cycle case
1class Solution:
2    def findMinDifference(self, timePoints: List[str]) -> int:
3        minutes=[60*int(num[:2])+ int(num[3:]) for num in timePoints]
4        minutes.sort()
5        ans=1e7
6        for i in range(len(minutes)-1):
7            ans=min(ans,minutes[i+1]-minutes[i])
8        ans=min(ans, 24*60-(minutes[-1]-minutes[0]))
9        return ans
10        