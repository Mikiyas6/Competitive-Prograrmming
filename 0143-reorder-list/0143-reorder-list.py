# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head):
            if not head or not head.next:
                return head
            
            second_part = head.next
            head.next = None
            reversed_second_part = reverse(second_part)
            current = reversed_second_part
            while current.next:
                current = current.next
            current.next = head
            return reversed_second_part
        middle = findMiddle(head)
        second_part = middle.next
        middle.next = None
        first_part = head
        reversed_second_part = reverse(second_part)
        def fun(part1,part2):
            if not part2:
                return part1
            if not part1.next and not part2.next:
                part1.next = part2
                return part1
            second_1 = part1.next
            part1.next = None
            second_2 = part2.next
            part2.next = None
            part1.next = part2
            part2.next = fun(second_1,second_2)
            return part1
        fun(first_part,reversed_second_part)