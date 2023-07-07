if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N):
        string = input()
        if "append" in string:
            listing = string.split()
            lists.append(int(listing[1]))
            listing = []
        elif "print" in string:
            print(lists)
        elif "remove" in string:
            listing = string.split()
            lists.remove(int(listing[1]))
            listing = []
        elif "insert" in string:
            listing = string.split()
            lists.insert(int(listing[1]),int(listing[2]))
            listing = []
        elif "sort" in string:
            lists = sorted(lists)
        elif "pop" in string:
            lists.pop()
        elif "reverse" in string:
            i = 0
            j = len(lists) - 1
            while i < j:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1
    
