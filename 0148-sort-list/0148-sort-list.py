# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        def findMiddle(current):
            
            slow = current
            fast = current.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def mergeSort(list1,list2):
            ptr1 = list1
            ptr2 = list2
            dummy = ListNode(-1)
            current = dummy

            def merge(current,ptr1,ptr2):

                if not ptr1:
                    current.next = ptr2
                    return current
                if not ptr2:
                    current.next = ptr1
                    return current
                
                if ptr1.val <= ptr2.val:
                    value = ptr1.val
                    ptr1 = ptr1.next
                else:
                    value = ptr2.val
                    ptr2 = ptr2.next
                
                node = ListNode(value)
                current.next = merge(node,ptr1,ptr2)
                return current
            
            return merge(current,ptr1,ptr2).next

        def fun(current):

            if not current or not current.next:
                return current
            
            middle = findMiddle(current)
            right_side = middle.next
            middle.next = None

            left = fun(current)
            right = fun(right_side)

            mergedList = mergeSort(left,right)

            return mergedList
        
        current = head
        return fun(current)
    
