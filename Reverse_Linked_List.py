# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        lists = []
        if (head == None):
            return None
        elif (current.next == None):
            return current
        else:
            while (current != None):
                lists.append(current.val)
                current = current.next
            print(lists)
            def insert_at_the_end(lists):
                if(len(lists) == 0):
                    return None
                else:    
                    value = lists[-1]
                    lists.pop(-1)
                    return ListNode(value,insert_at_the_end(lists)) 

            l2 = insert_at_the_end(lists)
            return l2

        
