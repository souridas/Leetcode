# Last updated: 3/5/2026, 8:07:00 AM
# group by and combine groups
1from collections import Counter
2class Solution:
3    def maxRepOpt1(self, text: str) -> int:
4        total_count=Counter(text)
5        if not total_count: return 0
6        groups=[]
7        curr_char=text[0]
8        count=0
9        for c in text:
10            if c==curr_char:
11                count+=1
12            else:
13                groups.append([curr_char,count])
14                curr_char=c
15                count=1
16        groups.append([curr_char,count])
17        ans=0
18        for i in range(len(groups)):
19            char,length=groups[i]
20            ans =max(ans,min(length+1,total_count[char]))
21            if i>0 and i<len(groups)-1 and groups[i-1][0]==groups[i+1][0] and groups[i][1]==1:
22                combined_length=groups[i-1][1]+groups[i+1][1]
23                ans=max(ans,min(combined_length+1,total_count[groups[i-1][0]]))
24        return ans
25
26            
27
28
29
30                