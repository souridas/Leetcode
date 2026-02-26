# Last updated: 2/26/2026, 3:03:56 PM
# monotonically increasing stack
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack=[]
4        ans_map={v:-1 for v in nums1}
5        for num in nums2:
6            while stack and num>stack[-1]:
7                top=stack.pop()
8                if top in ans_map:
9                    ans_map[top]=num
10            stack.append(num)
11        ans=[]
12        for v in nums1:
13            ans.append(ans_map[v])
14        return ans