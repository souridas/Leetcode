# Last updated: 3/30/2026, 10:34:56 PM
1class Solution:
2    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
3        MOD = 10**9 + 7
4        
5        # Boundary Check: It's impossible to see more people than exist (excluding pos)
6        if k > n - 1 or k < 0:
7            return 0
8            
9        def nCr(total_items: int, choose_items: int) -> int:
10            # Optimize to do the minimum number of multiplications
11            if choose_items > total_items // 2:
12                choose_items = total_items - choose_items
13                
14            num = 1
15            den = 1
16            
17            # Calculate permutation and factorial simultaneously
18            for i in range(choose_items):
19                num = (num * (total_items - i)) % MOD
20                den = (den * (i + 1)) % MOD
21                
22            # Use Fermat's Little Theorem for modular division
23            return (num * pow(den, -1, MOD)) % MOD
24
25        # We are choosing k people from the (n - 1) available people
26        ways_to_choose_visible = nCr(n - 1, k)
27        
28        # Multiply by 2 because the person at `pos` can choose 'L' or 'R'
29        total_assignments = (ways_to_choose_visible * 2) % MOD
30        
31        return total_assignments
32        