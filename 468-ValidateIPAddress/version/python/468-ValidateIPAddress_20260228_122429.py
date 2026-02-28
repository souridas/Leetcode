# Last updated: 2/28/2026, 12:24:29 PM
1class Solution:
2    def check_x_v4(self,x):
3        if len(x)>1 and x[0]=='0':
4            return False
5        if not x.isdigit():
6            return False
7        return int(x)>=0 and int(x)<=255
8    def check_x_v6(self,x):
9        if len(x)<1 or len(x)>4:
10            return False
11        hex_str="0123456789abcdef"
12        for c in x:
13            if c not in hex_str:
14                return False
15        return True
16    def validIPAddress(self, queryIP: str) -> str:
17        if "." in queryIP:
18            parts=queryIP.split('.')
19        else:
20            parts=queryIP.split(':')
21        if len(parts)==4:
22            for part in parts:
23                if not self.check_x_v4(part):
24                    return "Neither"
25            return "IPv4"
26        elif len(parts)==8:
27            for part in parts:
28                if not self.check_x_v6(part.lower()):
29                    return "Neither"
30            return "IPv6"
31        else:
32            return "Neither"
33
34        