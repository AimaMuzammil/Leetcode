# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                # Current level ka last node
                if i == level_size - 1:
                    result.append(node.val)

                # Left child
                if node.left:
                    q.append(node.left)

                # Right child
                if node.right:
                    q.append(node.right)

        return result
        