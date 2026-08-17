class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1


# | Iteration | `left` | `right` | Left value | Right value | `total` | Condition  | Action         |
# | --------- | -----: | ------: | ---------: | ----------: | ------: | ---------- | -------------- |
# | 1         |      0 |       3 |          2 |          15 |      17 | `17 > 9`   | `right--`      |
# | 2         |      0 |       2 |          2 |          11 |      13 | `13 > 9`   | `right--`      |
# | 3         |      0 |       1 |          2 |           7 |       9 | `9 == 9` ✅ | `return [1,2]` |
