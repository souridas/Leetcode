# Last updated: 2/21/2026, 9:44:09 AM
class MyQueue:

    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]
        

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        
    def pop(self) -> int:
        if len(self.pop_stack)==0:
            while len(self.push_stack):
                element=self.push_stack.pop()
                self.pop_stack.append(element)
            
        return self.pop_stack.pop()
   

    def peek(self) -> int:
        if len(self.pop_stack)==0:
            while len(self.push_stack):
                element=self.push_stack.pop()
                self.pop_stack.append(element)
        return self.pop_stack[-1]

    def empty(self) -> bool:
        if len(self.pop_stack)==0 and len(self.push_stack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()