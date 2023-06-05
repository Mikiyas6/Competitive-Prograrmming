class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = str(s)
        lists = string.split()
        for i in range(len(lists)):
            for j in range(len(lists)):
                if j == len(lists) - i - 1:
                    break
                elif int(lists[j+1][-1]) < int(lists[j][-1]):
                    self.swap(lists,j,j+1)
        for k in range(len(lists)):
            lists[k] = lists[k][:len(lists[k])-1]
        return ' '.join(lists)
    def swap(self,lists,x,y):
        temp = lists[x]
        lists[x] = lists[y]
        lists[y] = temp
        
        
            
            
