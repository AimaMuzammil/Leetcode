
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        answer = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                prev = stack.pop()
                answer[prev] = nums[i % n]
            if i < n:
                stack.append(i)
        return answer
        