from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)

        for sandwich in sandwiches:
            if sandwich not in queue:
                break

            while queue[0] != sandwich:
                queue.append(queue.popleft())

            queue.popleft()

        return len(queue)