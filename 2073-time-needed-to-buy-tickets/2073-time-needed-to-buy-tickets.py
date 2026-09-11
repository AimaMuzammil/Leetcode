class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()

        # Queue mein person ke indexes store karenge
        for i in range(len(tickets)):
            q.append(i)

        time = 0

        while q:
            # Front person
            i = q.popleft()
            
            # Person 1 ticket buy karta hai
            tickets[i] -= 1
            time += 1

            # Agar target person ke tickets khatam ho gaye
            if i == k and tickets[i] == 0:
                return time

            # Agar tickets abhi bhi baqi hain
            if tickets[i] > 0:
                q.append(i)