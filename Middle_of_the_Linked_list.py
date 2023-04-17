# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        counter = 0
        while (current != None):
            counter += 1
            current = current.next
        if (counter %2 == 0):
            middle = (counter/2) 
        else:
            middle = (counter//2) 
        current = head
        for i in range(middle):
            current = current.next
        return current
