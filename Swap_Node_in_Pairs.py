# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            current = head
            while current.next:
                if current == head:
                    next_node = current.next
                    current.next = next_node.next
                    next_node.next = current
                    head = next_node
                else:
                    next_node = current.next
                    current.next = next_node.next
                    previous.next = next_node
                    next_node.next = current
                previous = current
                current = current.next
                if not current:
                    break
        return head


# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         current = head
#         if current == None:
#             return None
#         elif current.next == None:
#             return head
#         pointer2 = current.next.next
#         head = head.next
#         head.next = current
#         current.next = pointer2
#         while(current.next != None):
#             pointer1 = current.next
#             if current.next.next == None:
#                 return head
            pointer2 = pointer1.next.next
            current.next = current.next.next
            current.next.next = pointer1
            pointer1.next = pointer2
            current = pointer1            
        return head
            
