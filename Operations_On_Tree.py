class LockingTree:
    def __init__(self, parent):
        self.parent = parent  
        self.n = len(parent)  
        self.locked = [-1] * self.n  
        self.children = [[] for _ in range(self.n)]  

        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, node, user):
        if self.locked[node] == -1:
            self.locked[node] = user
            return True
        return False

    def unlock(self, node, user):
        if self.locked[node] == user:
            self.locked[node] = -1
            return True
        return False

    def upgrade(self, node, user):
        if self.locked[node] == -1 and self.hasLockedDescendants(node) and not self.hasLockedAncestors(node):
            self.locked[node] = user
            self.unlockDescendants(node)
            return True
        return False

    def hasLockedDescendants(self, node):
        for child in self.children[node]:
            if self.locked[child] != -1:
                return True
            if self.hasLockedDescendants(child):
                return True
        return False

    def hasLockedAncestors(self, node):
        while node != -1:
            if self.locked[node] != -1:
                return True
            node = self.parent[node]
        return False

    def unlockDescendants(self, node):
        for child in self.children[node]:
            self.unlockDescendants(child)
            self.locked[child] = -1


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
