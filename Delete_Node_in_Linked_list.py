# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        lists = []
        current = node
        value_removed = current.val
        while(current != None):
            lists.append(current.val)
            current = current.next
        current = node
        for index,value in enumerate(lists):
            if value == value_removed:
                lists.pop(index)
        print(lists)
        while (current.next != None):
            current.val = lists[0]
            lists.pop(0)
            current = current.next
        current = node
        while(current.next != None):
            prev = current
            current = current.next
        prev.next = None
        
        

    
        
