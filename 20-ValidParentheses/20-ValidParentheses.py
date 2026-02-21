# Last updated: 2/21/2026, 9:45:17 AM
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        for c in s:
            if len(stack) and ((stack[-1]=='{' and c=='}') or (stack[-1]=='[' and c==']') or (stack[-1]=='(' and c==')')):
                stack.pop()
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        return False

        

        