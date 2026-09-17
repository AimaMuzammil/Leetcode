class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k#[1,0,0]#[1,2,0]#[1,2,3]
        self.capacity = k
        self.front = 0
        self.rear = -1
        self.count = 0#1#2#3
    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear  + 1) % self.capacity#-1+1%3
        self.queue[self.rear] = value
        self.count += 1
        return True
    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True
    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.count == self.capacity