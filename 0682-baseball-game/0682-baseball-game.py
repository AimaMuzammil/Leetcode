
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            
            # Sum of last two scores
            if op == "+":
                stack.append(stack[-1] + stack[-2])

            # Double previous score
            elif op == "D":
                stack.append(stack[-1] * 2)

            # Remove previous score
            elif op == "C":
                stack.pop()

            # Normal integer
            else:
                stack.append(int(op))

        return sum(stack)
        