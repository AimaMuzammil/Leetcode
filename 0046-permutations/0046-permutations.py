class Solution:
    def permute(self, nums):
        result = []
        path = []
        visited = [False] * len(nums)
        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                visited[i] = False
        backtrack()
        return result