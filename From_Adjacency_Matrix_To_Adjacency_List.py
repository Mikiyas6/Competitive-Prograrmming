import sys
n = int(sys.stdin.readline())
for i in range(n):
    row = list(map(int,input().split()))
    lists = []
    for index,element in enumerate(row):
        if element == 1:
            lists.append(index+1)
    string = str(len(lists)) + " "
    for j in range(len(lists)):
        string += str(lists[j]) + " "
    print(string)
