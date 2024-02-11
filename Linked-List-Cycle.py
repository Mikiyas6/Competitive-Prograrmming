# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        tortoise = head
        rabbit = head

        # Phase 1 Find if there's a Cycle

        while rabbit and rabbit.next:

            tortoise = tortoise.next
            rabbit = rabbit.next.next

            if tortoise == rabbit:

                return True
                # break
        
        # if slow != fast:

        #     return False
        
        # Phase 2 Find the start of the cycle

        # slow = head

        # while rabbit and rabbit.next:

        #     tortoise = tortoise.next
        #     rabbit = rabbit.next

        #     if tortoise == rabbit:

        #         return Tortoise
