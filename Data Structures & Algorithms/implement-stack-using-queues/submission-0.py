class MyStack:

    def __init__(self):
        self.helper = []
        self.stack = []
#h.      t
#1,2,3,4,5
#5,4,3,2,1

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def empty(self) -> bool:
        return False if len(self.stack) > 0 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()