class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.lists = []
        self.limit = k
        self.size = 0
    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        lists1 = []
        if (len(self.lists) == 0):
            self.lists.append(value)
            self.size += 1
            return True
        elif (len(self.lists) == self.limit):
            return False
        elif (len(self.lists) < self.limit):
            while(len(self.lists) > 0):
                lists1.append(self.lists[-1])
                self.lists.pop(-1)
            self.lists = []
            lists1.append(value)
            while(len(lists1) > 0):
                self.lists.append(lists1[-1])
                lists1.pop(-1)
            self.size += 1
            return True
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if (len(self.lists) < self.limit):
            self.lists.append(value)
            self.size += 1
            return True
        else:
            return False
    def deleteFront(self):
        """
        :rtype: bool
        """
        if (len(self.lists) == 0):
            return False
        else:
            self.lists.pop(0)
            self.size -= 1
            return True
    def deleteLast(self):
        """
        :rtype: bool
        """
        if (len(self.lists) == 0):
            return False
        else:
            self.lists.pop(-1)
            self.size -= 1
            return True
    def getFront(self):
        """
        :rtype: int
        """
        if (len(self.lists) == 0):
            return -1
        else:
            return self.lists[0]
    def getRear(self):
        """
        :rtype: int
        """
        if (len(self.lists) == 0):
            return -1
        else:
            return self.lists[-1]
    def isEmpty(self):
        """
        :rtype: bool
        """
        if (len(self.lists) == 0):
            return True
        else:
            return False
    def isFull(self):
        """
        :rtype: bool
        """
        if (len(self.lists) == self.limit):
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
