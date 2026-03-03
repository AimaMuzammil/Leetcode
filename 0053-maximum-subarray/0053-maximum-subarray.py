class Solution(object):
    def maxSubArray(self, nums):
        maxSum = float('-inf')
        sums = 0 
        for i in range(len(nums)):
            sums = sums + nums[i]
            maxSum = max(sums , maxSum)
            if (sums <0) :
               sums = 0 
        return maxSum


        