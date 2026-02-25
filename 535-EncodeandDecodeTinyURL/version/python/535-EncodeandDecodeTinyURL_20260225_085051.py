# Last updated: 2/25/2026, 8:50:51 AM
# hashmap
1from collections import defaultdict
2import random
3class Codec:
4    def __init__(self):
5        self.hash_map=defaultdict(str)
6    def encode(self, longUrl: str) -> str:
7        """Encodes a URL to a shortened URL.
8        """
9        encoded_url='ttp://tinyurl.com/'+str(len(longUrl))
10        self.hash_map[encoded_url]=longUrl
11        return encoded_url
12        
13
14    def decode(self, shortUrl: str) -> str:
15        """Decodes a shortened URL to its original URL.
16        """
17        return self.hash_map[shortUrl]
18        
19
20# Your Codec object will be instantiated and called as such:
21# codec = Codec()
22# codec.decode(codec.encode(url))