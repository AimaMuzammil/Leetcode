# class Solution(object):
#     def letterCombinations(self, digits):
#         if not digits:
#             return []
#         phone = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }
#         result = []
#         def backtrack(index, current):
#             # combination complete
#             if index == len(digits):
#                 result.append(current)
#                 return
#             letters = phone[digits[index]]
#             for letter in letters:
#                 # choose
#                 backtrack(index + 1, current + letter)
#         backtrack(0, "")
#         return result


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def backtrack(index, current):
            # Base case
            if index == len(digits):
                result.append("".join(current))
                return
            # Try every letter of current digit
            for letter in phone[digits[index]]:
                # Choose
                current.append(letter)
                # Explore
                backtrack(index + 1, current)
                # Undo
                current.pop()
        backtrack(0, [])
        return result