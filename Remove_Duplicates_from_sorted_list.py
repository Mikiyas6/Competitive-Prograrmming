# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            left = head
            right = left.next
            while right:
                if left.val == right.val:
                    right = right.next
                    left.next = right
                else:
                    left = left.next
                    right = right.next
        return head
        
        # current = head
        # if current == None:
        #     return None
        # elif current.next == None:
        #     return head
        # value = current.val
        # while(current.next != None):
        #     if (value != current.next.val):
        #         current = current.next
        #         value = current.val
        #     else:
        #             current.next = current.next.next
        # return head
        # Definition for singly-linked list.
        




















       

                    





        
        
        

            
        


    
