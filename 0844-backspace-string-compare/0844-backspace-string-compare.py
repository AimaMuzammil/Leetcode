class Solution(object):
    def backspaceCompare(self, s, t):

        def process(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)
        return process(s) == process(t)