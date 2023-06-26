class Solution  (object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        reverse_popped = []
        for i in range(len(popped)-1,-1,-1):
            reverse_popped.append(popped.pop())
        popped = reverse_popped
        lists = []
        i = 0
        while len(popped) > 0:
            if pushed[i] != popped[-1]:
                lists.append(pushed[i])
            elif pushed[i] == popped[-1]:
                popped.pop()
                if len(lists) == 0:
                    i += 1
                    continue
                for j in range(len(lists)-1,-1,-1):
                    if popped[-1] == lists[j]:
                        lists.pop()
                        popped.pop()
                    elif popped[-1] in lists and  popped[-1] != lists[-1]:
                        return False
                    else:
                        break
            i += 1
        return True
        
            

        
        

        
