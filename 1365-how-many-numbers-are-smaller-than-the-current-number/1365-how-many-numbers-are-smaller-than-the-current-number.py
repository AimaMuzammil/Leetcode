class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        count = {} 
        for i in range (len(sorted_nums)): 
            if sorted_nums[i] not in count: 
                count[sorted_nums[i]] = i
                
        return [count[num] for num in nums] 

# Solution 02:
#     sorted_nums = sorted(nums)
#         ans = []

#         for num in nums:
#             ans.append(sorted_nums.index(num))

#         return ans