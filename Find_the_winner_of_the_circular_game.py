class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_of_friends = list(range(1,n+1))
        i = k - 1
        while len(list_of_friends) > 1:
            while i >= len(list_of_friends):
                    i = i - len(list_of_friends) 
            list_of_friends.pop(i)
            i += k - 1        
        return list_of_friends[0]
        
