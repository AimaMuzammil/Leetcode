class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                nge[smaller] = num
            stack.append(num)
        # remaining elements
        while stack:
            nge[stack.pop()] = -1
        # build answer
        ans = []
        for num in nums1:
            ans.append(nge[num])
        return ans
        