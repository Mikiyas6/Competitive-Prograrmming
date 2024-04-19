# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:

            return l2
        
        if not l2:

            return l1
        
        def reverse(head):

            if not head or not head.next:

                return head
            
            second_part = head.next
            head.next = None
            first_node = head

            reversed_second_part = reverse(second_part)

            current = reversed_second_part

            while current.next:

                current = current.next
            
            current.next = first_node

            return reversed_second_part
        
        l1_reversed = reverse(l1)
        l2_reversed = reverse(l2)

        dummy = ListNode(-1)
        current = dummy

        def fun(current,ptr1, ptr2,carry):

            if not ptr1 and not ptr2:

                if carry != 0:

                    Node = ListNode(carry)
                    current.next = Node
                    return current

            if not ptr1:

                original = current
                while ptr2:

                    total = ptr2.val + carry

                    result = total % 10
                    carry = total // 10

                    Node = ListNode(result)
                    current.next = Node
                    current = Node
                    ptr2 = ptr2.next
                
                if carry != 0:

                    current.next = ListNode(carry)
            
                return original
            
            if not ptr2:

                original = current
                while ptr1:

                    total = ptr1.val + carry

                    result = total % 10
                    carry = total // 10

                    Node = ListNode(result)
                    current.next = Node
                    current = Node
                    ptr1 = ptr1.next
                
                if carry != 0:

                    current.next = ListNode(carry)
            
                return original

            total = ptr1.val + ptr2.val + carry

            result = total % 10
            carry = total // 10

            print(total,result,carry)

            Node = ListNode(result)

            current.next = fun(Node,ptr1.next,ptr2.next,carry)

            return current
        
        output = fun(current,l1_reversed,l2_reversed,0).next
        reversed_output = reverse(output)
        return reversed_output
            


