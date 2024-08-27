class Stack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self):
        if self.data is not []:
            temp = self.data[-1]
            self.data = self.data[0:-1]
            return temp
        else:
            return None

    def size(self) -> int:
        return len(self.data)

    def peek(self):
        if self.data is not []:
            return self.data[-1]
        else:
            return None


class MyQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, x: int) -> None:
        self.first_stack.push(x)

    def pop(self) -> int:
        while self.first_stack.size() is not 0:
            char = self.first_stack.pop()
            self.second_stack.push(char)
        temp = self.second_stack.pop()
        while self.second_stack.size() is not 0:
            char = self.second_stack.pop()
            self.first_stack.push(char)
        return temp

    def peek(self) -> int:
        while self.first_stack.size() is not 0:
            char = self.first_stack.pop()
            self.second_stack.push(char)
        temp =  self.second_stack.peek()
        while self.second_stack.size() is not 0:
            char = self.second_stack.pop()
            self.first_stack.push(char)
        return temp

    def empty(self) -> bool:
        return self.first_stack.size() == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
