# Last updated: 2/21/2026, 9:44:53 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        store=[1]*(n+1)
        for i in range(2,n+1):
            store[i]=store[i-1]+store[i-2]
        return store[n]
        