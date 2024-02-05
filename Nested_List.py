if __name__ == '__main__':
    
    from collections import defaultdict
    
    hashmap = defaultdict(list)
    
    lists = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        hashmap[score].append(name)
        
        lists.append(score)
    
    lists.sort()
    
    second_lowest = 0
    
    for i in range(len(lists)):
        
        if lists[i] != lists[i+1]:
            
            second_lowest = lists[i+1]
            
            break
    
    list_of_names = hashmap[second_lowest]
    
    list_of_names.sort()
    
    for names in list_of_names:
        
        print(names)
    
    
