def makeGraph(filename):
    graph = {}
    with open(filename) as f:
        edges = [line.strip().split('-') for line in f]
    for edge in edges:
        i, j = edge[0], edge[1]
        if i not in graph:
            graph[i] = []
        if j not in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)
    return graph

def findAllPaths(graph, start, end):
    paths = []
    stack = [[start]]
    while len(stack) > 0:
        path = stack.pop()
        current = path[-1]

        if current == end:
            paths.append(path)
        else: 
            for neighbor in graph[current]:
                if neighbor.lower() not in path:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    stack.append(new_path)
    print(paths)
    return len(paths)

graph = makeGraph('input1212.txt')
paths = findAllPaths(graph, 'start', 'end')
print(paths)