class Solution:
    def runningSum(self, nums):
        for i in range (1, len(nums)):
             nums[i] = nums[i]+ nums[i-1]
        return nums

        # result = []
        # for i in range (len(nums)):
        #     result.append (sum(nums[:i+1]))
        # return result 
       