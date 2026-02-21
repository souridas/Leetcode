# Last updated: 2/21/2026, 9:44:55 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            m=len(b)-len(a)
            a="0"*m + a
        else:
            m=len(a)-len(b)
            b="0"*m + b
        ans=[]
        carry=0
        for i in range(len(b)-1,-1,-1):
            val=carry+int(a[i])+int(b[i])
            ans.append(str(val%2))
            carry=val//2
        if carry:
            ans.append(str(carry))
        ans.reverse()

        return "".join(ans)
        

            

        