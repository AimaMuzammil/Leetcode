class StockSpanner:
    def __init__(self):
        self.stack = []
        self.index = -1      #use this just once when stockspanner is created
    def next(self, price: int) -> int:
        self.index += 1    #moves to the next price/day.
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:     #if stack is empty
            span = self.index + 1   #[0]
        else:
            span = self.index - self.stack[-1][1]
        self.stack.append((price,self.index))
        return span

# Time limit exceed!
# class StockSpanner:
#     def __init__(self):
#         self.stack = []#[100,80]
#     def next(self, price: int) -> int:
#         self.stack.append(price)#[100,80,60,70,60,75]
#         span = 1
#         i = len(self.stack) - 2#[-1,0,1,2,3,4,5]   #1-2...2-2...3-2...
#         while i >= 0 and self.stack[i] <= price:
#             span += 1#[2][4]
#             i -= 1
#         return span