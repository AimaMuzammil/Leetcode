# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):

        # Store each value's position in inorder
        inorder_index = {
            value: i for i, value in enumerate(inorder)
        }

        # Keeps track of the next root in preorder
        self.pre_index = 0

        def build(left, right):

            # No elements left for this subtree
            if left > right:
                return None

            # Get the root from preorder
            root_value = preorder[self.pre_index]
            self.pre_index += 1

            # Create the root node
            root = TreeNode(root_value)

            # Find the root's position in inorder
            mid = inorder_index[root_value]

            # Build the left subtree
            root.left = build(left, mid - 1)

            # Build the right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)


        