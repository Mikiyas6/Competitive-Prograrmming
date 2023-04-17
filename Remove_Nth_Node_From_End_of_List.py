# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        counter = 0
        if (current.next == None):
            return None
        while(current != None):
            counter += 1
            current = current.next
        current = head
        from_start = counter - n
        for i in range(1,counter):
            if (from_start == 0):
                head = current.next
            elif i == from_start:
                current.next = current.next.next
                break
            else:
                current = current.next
        return head
        
