# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        heapify(minHeap)
        for linkedList in lists:
            current = linkedList
            while current:
                heappush(minHeap,current.val)
                current = current.next
        dummy = ListNode(-1)
        current = dummy
        while minHeap:
            value = heappop(minHeap)
            current.next = ListNode(value)
            current = current.next
        return dummy.next
