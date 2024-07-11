# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        def mergeSorted(arr1,arr2):

            dummy = ListNode(-1)
            current = dummy
            node1, node2 = arr1, arr2

            while node1 and node2:
                
                if node1.val <= node2.val:
                    value = node1.val
                    node1 = node1.next
                else:
                    value = node2.val
                    node2 = node2.next
                
                current.next = ListNode(value)
                current = current.next

            if not node1:
                current.next = node2
            if not node2:
                current.next = node1
            return dummy.next

        sortedArr = None
        for node in lists:
            sortedArr = mergeSorted(sortedArr,node)
        return sortedArr