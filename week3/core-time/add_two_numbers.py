# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        차례로 더하면서 올림을 저장해보자
        숫자 * 1, 숫자 * 10, 숫자 * 100
        
        차례로 나머지 100, 10, 1하면서 리스트로 만들어보자
        (자릿수를 함께 저장해야 하나?)
        """
        digits = 1
        total = 0
        carry = 0
        node1 = l1
        node2 = l2
        length = 0
        while node1 or node2:
            sum = node1.val + node2.val + carry
            if sum // 10 == 1:
                carry = 1
            else:
                carry = 0
            total += sum * digits
            node1 = node1.next
            node2 = node2.next
            digits *= 10
            length += 1

        while node1:
            sum = node1.val + carry
            if sum // 10 == 1:
                carry = 1
            else:
                carry = 0
            total += sum * digits
            node1 = node1.next
            digits *= 10
            length += 1

        while node2:
            sum = node2.val + carry
            if sum // 10 == 1:
                carry = 1
            else:
                carry = 0
            total += sum * digits
            node2 = node2.next
            digits *= 10
            length += 1


        digit = 10**length
        value = total % digit
        head = ListNode(value)
        digit //= 10
        while (length - 1) != 0:
            value = total % digit
            head.next = ListNode(value)
            digit //= 10
            length -= 1
        return head

