import sys
n = int(sys.stdin.readline())
adjacency_matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
flag = True
sources, sinks = [], []
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[0])):
        if adjacency_matrix[j][i] == 1:
            flag = False
            break
    if flag:
        sources.append(i+1)
    flag = True
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[0])):
        if adjacency_matrix[i][j] == 1:
            flag = False
            break
    if flag:
        sinks.append(i+1)
    flag = True
string1 = str(len(sources)) + " "
string2 = str(len(sinks)) + " "
for i in range(len(sources)):
    string1 += str(sources[i]) + " "
for i in range(len(sinks)):
    string2 += str(sinks[i]) + " "
print(string1)
print(string2)
