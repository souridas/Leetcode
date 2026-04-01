# Last updated: 4/1/2026, 4:26:11 PM
# voting algorithm, find the top k frequent elements
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        a,b=float('-inf'),float('-inf')
4        cnt1,cnt2=0,0
5        for num in nums:
6            if cnt1==0 and num!=b:
7                a=num
8                cnt1=1
9            elif cnt2==0 and num!=a:
10                b=num
11                cnt2=1
12            elif num==a:
13                cnt1+=1
14            elif num==b:
15                cnt2+=1
16            else:
17                cnt1-=1
18                cnt2-=1
19        cnt1,cnt2=0,0
20        for num in nums:
21            if num==a:
22                cnt1+=1
23            if num==b:
24                cnt2+=1
25        target=len(nums)//3+1
26        ans=[]
27        if cnt1>=target:
28            ans.append(a)
29        if cnt2>=target and a!=b:
30            ans.append(b)
31        return ans
32
33        