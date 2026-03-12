# Last updated: 3/12/2026, 9:08:34 AM
# bellman ford
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        prices=[float('inf')]*n
4        prices[src]=0
5        for _ in range(k+1):
6            tmp_prices=prices.copy()
7            for u,v,price in flights:
8                if prices[u]!=float('inf') and prices[u]+price<tmp_prices[v]:
9                    tmp_prices[v]=prices[u]+price
10            prices=tmp_prices
11        if prices[dst]==float('inf'):
12            return -1
13        return prices[dst]
14
15        