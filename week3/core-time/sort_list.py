# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ??? 시간 복잡도 O(nlogn), 공간 복잡도 O(1)이 된다고??
        """
        (시작)
        4 - 2 - 1 - 3
        2 - 1 - 3 - 4
        1 - 2 - 3 - 4

        -1 - 5 - 3 - 4 - 0
        -1 - 3 - 4 - 0 - 5
        -1 - 3 - 0 - 4 - 5
        -1 - 0 - 3 - 4 - 5

        o o x x o o x x o o
        o x o x o x o x o x
        """

        node = head
        while ?:
            next_node = node.next
            if next_node.val < node.val:
                next_node.val, node.val = node.val, next_node.val
            node = next_node
