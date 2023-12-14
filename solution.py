def find_root_vertex(graph):
    in_degree = [0] * len(graph)
    out_degree = [0] * len(graph)               

    for u in range(len(graph)):
        for v in graph[u]:                       
            out_degree[u] += 1
            in_degree[v] += 1

    for u in range(len(graph)):
        if in_degree[u] == 0 and out_degree[u] > 0:
            return u

    return -1

file_path = 'input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

    max_vertex = max(max(map(int, line.strip().split()[:2])) for line in lines)
    graph = [[] for _ in range(max_vertex + 1)]

    for line in lines:
        values = list(map(int, line.strip().split()))
        if len(values) < 2:
            print(f"Skipping invalid line: {line}")
            continue

        u, v = values[:2]  
        graph[u].append(v)

root_vertex = find_root_vertex(graph)

with open('output.txt', 'w') as file:
    file.write(str(root_vertex))