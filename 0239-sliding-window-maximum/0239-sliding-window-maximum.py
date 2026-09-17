from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()#[1,2]   # stores indexes
        result = []
        for i in range(len(nums)):
            #Remove indexes that are outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            #Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:#values on these indexes
                dq.pop()
            #Add current index
            dq.append(i)
            #Once first window is complete, add maximum
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result