# Last updated: 2/21/2026, 9:44:21 AM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res=""
        while(columnNumber):
            res+=dic[(columnNumber-1)%26]
            columnNumber=(columnNumber-1)//26
        return res[::-1]