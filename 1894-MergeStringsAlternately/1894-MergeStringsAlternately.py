# Last updated: 2/21/2026, 9:43:07 AM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i in range(len(word1)):
            s+=word1[i]
            if i<len(word2):
                s+=word2[i]
        if len(word1)<len(word2):
            s+=word2[len(word1):]
        return s