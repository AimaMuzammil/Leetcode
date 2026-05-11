
class MyQueue:

    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()  # ensure stack2 has correct order
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def empty(self) -> bool:
        return not self.stack1  and not  self.stack2 

    
# class MyQueue:
#     def __init__(self):
#         self.queue = []

#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         return self.queue.pop(0)

#     def peek(self) -> int:
#         return self.queue[0]

#     def empty(self) -> bool:
#         return not self.queue