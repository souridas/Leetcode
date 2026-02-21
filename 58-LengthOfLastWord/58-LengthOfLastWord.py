# Last updated: 2/21/2026, 9:44:59 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(" ").split(" ")[-1])
            
        