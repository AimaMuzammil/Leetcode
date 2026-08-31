class Solution(object):
    def isPossibleToSplit(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] > 2:
               return False

        return True

# START
# Create an empty frequency map
# For every number in nums:
#     count its frequency
#     If frequency of this number > 2:
#         return false
# Return true
# END
    