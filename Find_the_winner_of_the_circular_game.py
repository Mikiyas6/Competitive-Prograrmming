class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_of_friends = []
        for i in range(1,n+1):
            list_of_friends.append(i)
        i = k % n - 1
        if i < 0:
            i = i + len(list_of_friends)
        while len(list_of_friends) > 1:
            list_of_friends.pop(i)
            print(i,list_of_friends)
            i += k - 1
            if i >= len(list_of_friends):
                i = i - len(list_of_friends)
                while i >= len(list_of_friends):
                    i = i - len(list_of_friends) 
        return list_of_friends[0]
        
