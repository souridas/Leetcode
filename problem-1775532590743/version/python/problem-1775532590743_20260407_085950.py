# Last updated: 4/7/2026, 8:59:50 AM
1class Solution:
2    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
3        # 1. Count the two different types of mismatches
4        # diff01: indices where s[i] == '0' and t[i] == '1'
5        # diff10: indices where s[i] == '1' and t[i] == '0'
6        diff01 = 0
7        diff10 = 0
8        
9        for c1, c2 in zip(s, t):
10            if c1 == '0' and c2 == '1':
11                diff01 += 1
12            elif c1 == '1' and c2 == '0':
13                diff10 += 1
14                
15        mx = max(diff01, diff10)
16        mn = min(diff01, diff10)
17        total_mismatches = diff01 + diff10
18        
19        # Strategy 1: Ignore swaps entirely and just flip every mismatched character.
20        ans = total_mismatches * flipCost
21        
22        # Strategy 2: Use intra-string swaps to fix pairs of opposite mismatches.
23        # One swap in `s` fixes a (0->1) mismatch and a (1->0) mismatch at the same time.
24        # Any leftover mismatches are handled with flips.
25        ans = min(ans, mn * swapCost + (mx - mn) * flipCost)
26        
27        # Strategy 3: Use cross-swaps to "balance" the mismatch types.
28        # A cross-swap turns a (0->1) mismatch into a (1->0) mismatch (or vice versa).
29        # By balancing them, we maximize the number of pairs we can fix with `swapCost`.
30        avg_pairs = total_mismatches // 2
31        
32        # How many cross-swaps we need to reach the perfectly balanced state
33        cross_swaps_needed = avg_pairs - mn
34        
35        # If the total mismatches is odd, 1 mismatch will be left completely unpaired
36        unpaired_leftover = total_mismatches - 2 * avg_pairs
37        
38        cost3 = (cross_swaps_needed * crossCost) + (avg_pairs * swapCost) + (unpaired_leftover * flipCost)
39        
40        ans = min(ans, cost3)
41        
42        return ans