# Last updated: 2/26/2026, 9:21:26 AM
# hashmap
1from collections import defaultdict
2class Solution:
3    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
4        hash_map=defaultdict(int)
5        for domain in cpdomains:
6            splitted=domain.split(' ')
7            domain_vist=splitted[0]
8            web_domain=splitted[1]
9            web_domain_splits=web_domain.split('.')
10            sub_domain=web_domain_splits[-2]+"."+web_domain_splits[-1]
11            hash_map[sub_domain]+=int(domain_vist)
12            hash_map[web_domain_splits[-1]]+=int(domain_vist)
13
14            if len(web_domain_splits)>2:
15                i=1
16                while i>0:
17                    sub_domain=web_domain_splits[i-1] +"."+sub_domain
18                    i-=1
19                    hash_map[sub_domain]+=int(domain_vist)
20        ans=[]
21        for k,v in hash_map.items():
22            ans.append(str(v)+" "+k)
23        return ans
24        
25        