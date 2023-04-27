# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lists = []
        current = head
        while(current != None):
            lists.append(current.val)
            current = current.next
        while(len(lists) > 0):
            if (lists[0] == lists[-1] and len(lists) > 1):
                lists.pop(0)
                lists.pop(-1)
                continue
            elif(len(lists) == 1):
                return True
            else:
                return False
        return True
