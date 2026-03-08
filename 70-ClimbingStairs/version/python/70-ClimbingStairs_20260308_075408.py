# Last updated: 3/8/2026, 7:54:08 AM
# stairs(n)=stairs(n-1)+stairs(n-2)
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        store=[0]*(n+1)
4        if n<=1:
5            return n
6        store[1]=1
7        store[2]=2
8        for i in range(3,n+1):
9            store[i]=store[i-1]+store[i-2]
10        return store[n]
11
12        
13        