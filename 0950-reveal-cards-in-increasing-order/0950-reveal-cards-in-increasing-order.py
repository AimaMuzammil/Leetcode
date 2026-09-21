class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort() 
        n=len(deck) 
        que=deque(range(n)) 
        res=[0]*(n) 
        for no in deck: 
            res[que.popleft()]=no 
            if que:
             que.append(que.popleft())
        return res
        
    