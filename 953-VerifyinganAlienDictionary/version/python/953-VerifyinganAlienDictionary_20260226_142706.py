# Last updated: 2/26/2026, 2:27:06 PM
1from collections import defaultdict
2class Solution:
3    def isAlienSorted(self, words: List[str], order: str) -> bool:
4        alpha_map=defaultdict(int)
5        for i,c in enumerate(order):
6            alpha_map[c]=i
7        encoded_list = [[alpha_map[c] for c in w] for w in words]
8        return all(w1<=w2 for w1,w2 in zip(encoded_list,encoded_list[1:]))
9            
10
11
12        