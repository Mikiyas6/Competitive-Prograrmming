if __name__ == '__main__':
    N = int(input())
    
    lists = []
    
    for i in range(N):
        
        things_to_do = list(input().split())
        
        command = things_to_do[0]
        
        if command == "insert":
            
            lists.insert(int(things_to_do[1]),int(things_to_do[2]))
            
        elif command == "print":
            
            print(lists)
        
        elif command == "remove":
            
            lists.remove(int(things_to_do[1]))
        
        elif command == "append":
            
            lists.append(int(things_to_do[1]))
        
        elif command == "sort":
            
            lists.sort()
        
        elif command == "pop":
            
            lists.pop()
            
        elif command == "reverse":
            
            lists.reverse()
        
        
    
