# Last updated: 2/26/2026, 2:49:14 PM
1class Solution:
2    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
3        words=text.split(" ")
4        i=0
5        ans=[]
6        while i<len(words)-2:
7            if words[i]==first and words[i+1]==second:
8                if words[i+2]:
9                    ans.append(words[i+2])
10            i+=1
11
12        return ans
13
14        