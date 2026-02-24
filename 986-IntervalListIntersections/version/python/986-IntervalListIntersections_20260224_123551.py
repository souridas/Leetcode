# Last updated: 2/24/2026, 12:35:51 PM
# check the intersection condition and then find start and end of intersection and iterate
1class Solution:
2    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
3        i,j=0,0
4        result=[]
5        while i<len(firstList) and j<len(secondList):
6            a_start,a_end=firstList[i]
7            b_start,b_end=secondList[j]
8            if a_start<=b_end and b_start<=a_end:
9                result.append([max(a_start,b_start),min(a_end,b_end)])
10            if a_end<=b_end:
11                i+=1
12            else:
13                j+=1
14        return result
15        