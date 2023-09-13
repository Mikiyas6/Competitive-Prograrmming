def is_bicolourable(graph, n):
    # An array to represent the color of each node, initialized with -1 (uncolored)
    node_colors = [-1] * n
    node_colors[0] = 0  
    stack = [0]  

    while stack:
        current_node = stack.pop()

        
        for neighbor in graph[current_node]:
            if node_colors[neighbor] == -1:
                node_colors[neighbor] = 1 - node_colors[current_node]  
                stack.append(neighbor)
            elif node_colors[neighbor] == node_colors[current_node]:
                return False  
    return True  

while True:
    n = int(input())
    if n == 0:
        break

    l = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(l):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    if is_bicolourable(graph, n):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
