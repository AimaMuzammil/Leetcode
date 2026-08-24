# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # 3. Merge both halves
        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
        