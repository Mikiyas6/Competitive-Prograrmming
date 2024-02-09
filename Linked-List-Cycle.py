# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        tortoise = head
        rabbit = head

        # Phase 1

        while rabbit and rabbit.next:

            tortoise = tortoise.next
            rabbit = rabbit.next.next

            if tortoise == rabbit:

                break
        
        # Phase 2

        while rabbit and rabbit.next:

            tortoise = tortoise.next
            rabbit = rabbit.next

            if tortoise == rabbit:

                return True
