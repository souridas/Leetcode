# Last updated: 3/8/2026, 8:25:42 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        if not s or s[0]=='0':
4            return 0
5        n=len(s)
6        store=[0]*(n+1)
7        store[0]=1
8        store[1]=1
9        for i in range(2,n+1):
10            if s[i-1]!='0':
11                store[i]+=store[i-1]
12            two_digit = int(s[i-2:i])
13            if 10 <= two_digit <= 26:
14                store[i] += store[i-2]
15        return store[n]       