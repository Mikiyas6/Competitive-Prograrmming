# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if current == None:
            return None
        elif current.next == None:
            return head
        value = current.val
        while(current.next != None):
            if (value != current.next.val):
                current = current.next
                value = current.val
            else:
                    current.next = current.next.next
        return head
        




















       

                    





        
        
        

            
        


    
