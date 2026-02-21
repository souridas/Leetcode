# Last updated: 2/21/2026, 9:44:56 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-2
        carry=0
        if digits[-1]==9:
            digits[-1]=0
            carry=1
        else:
            digits[-1]+=1
            return digits
        while i>=0:
            if digits[i]!=9 :
                if carry==0:
                    return digits
                else:
                    digits[i]+=carry
                    carry=0
            elif digits[i]==9 and carry==1:
                digits[i]=0
                carry=1
            i-=1
        if carry==1:
            return [1]+digits
        else:
            return digits
            
        
        