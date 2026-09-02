class Solution:
    def nextGreaterElement(self, n):
        digits = list(str(n))

        # Step 1: Find the pivot
        i = len(digits) - 2

        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # No greater number possible
        if i < 0:
            return -1

        # Step 2: Find the smallest greater digit
        j = len(digits) - 1

        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the right side
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))

        # Check 32-bit integer limit
        if result > 2**31 - 1:
            return -1

        return result