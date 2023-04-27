# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lists1 = []
        lists2 = []
        lists3 = []
        lists4 = []
        listsA = []
        listsB = []
    
        while (l1 != None):
            listsA.append(l1.val)
            l1 = l1.next
        while (l2 != None):
            listsB.append(l2.val)
            l2 = l2.next
        
        lists1 = listsA
        lists2 = listsB
        
            
        diff = 0
        remainder = 0
            
        if (len(lists1) > len(lists2)):
            diff = len (lists1) - len (lists2)
            for i in range(diff):
                lists2.append(0)
        elif (len(lists1) < len (lists2)):
            diff = len (lists2) - len (lists1)
            for j in range (diff):
                lists1.append(0)
        for k in range(len(lists1)):
            if (lists1[k] + lists2[k] + remainder <= 9):
                lists3.append(lists1[k] + lists2[k] + remainder)
                remainder = 0
            else:
                tenth = int((str(lists1[k] + lists2[k] + remainder))[0])
                ones = int((str(lists1[k] + lists2[k] + remainder))[1])
                lists3.append(ones)
                remainder = tenth
        if(remainder > 0):      
            lists3.append(remainder)
        
        def insert_at_the_end(lists):
            if(len(lists) == 0):
                return None
            else:    
                value = lists[0]
                lists.pop(0)
                return ListNode(value,insert_at_the_end(lists)) 

        l3 = insert_at_the_end(lists3)

        return l3

        

            
