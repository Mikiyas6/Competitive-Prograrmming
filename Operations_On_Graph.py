import sys
from collections import defaultdict
dictionary = defaultdict(list)
def Add_Edge(u,v):
    dictionary[u].append(v)
    dictionary[v].append(u)
def vertex(u):
    lists = dictionary[u]
    string = ""
    for i in range(len(lists)):
        string += str(lists[i]) + " "
    print(string)
number_of_nodes = int(sys.stdin.readline())
number_of_operations = int(sys.stdin.readline())
for i in range(number_of_operations):
    row = list(map(int,sys.stdin.readline().split()))
    if row[0] == 1:
        Add_Edge(row[1],row[2])
    else:
        vertex(row[1])
# 4
# 4
# 1 1 2
# 1 2 3
# 2 4
# 2 2
