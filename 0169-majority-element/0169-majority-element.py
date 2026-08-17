# class Solution:
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > len(nums) // 2:
                return num

# 1. Empty dictionary banao
#         ↓
# 2. Array ke elements one-by-one dekho
#         ↓
# 3. Agar number pehle nahi mila:
#        count = 1
#         ↓
# 4. Agar pehle mil chuka hai:
#        count + 1
#         ↓
# 5. Har counting ke baad check:
#        kya count > n/2 ?
#         ↓
# 6. Yes → return number