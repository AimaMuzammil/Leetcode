class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            # Opening bracket
            if char in "([{":
                stack.append(char)
            # Closing bracket
            else:
                # Stack empty hai
                if not stack:
                    return False
                # Top bracket match nahi karta
                if stack[-1] != pairs[char]:
                    return False
                # Match ho gaya, remove karo
                stack.pop()
        # Agar stack empty hai to valid
        return len(stack) == 0