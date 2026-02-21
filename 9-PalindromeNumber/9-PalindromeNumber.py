# Last updated: 2/21/2026, 9:45:26 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
            temp=0
            y=x
            while x>0 :
                temp=temp*10+x%10
                x=x//10
            if y==temp:
                return True
            else:
                return False
        
        