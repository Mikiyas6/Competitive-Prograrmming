# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for node in lists:
            current = node
            while current:
                heappush(heap,current.val)
                current = current.next
        
        dummy = ListNode(-1)
        current = dummy
        while heap:
            current.next = ListNode(heappop(heap))
            current = current.next
        return dummy.next
