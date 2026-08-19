class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        used = [False] * len(nums)
        def backtrack(current):
            # permutation complete
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                # 1. Agar number already use ho chuka hai
                if used[i]:
                    continue
                # 2. Duplicate ko same level par skip karo
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                # choose
                used[i] = True
                current.append(nums[i])
                # explore
                backtrack(current)
                # undo / backtrack
                current.pop()
                used[i] = False
        backtrack([])
        return result