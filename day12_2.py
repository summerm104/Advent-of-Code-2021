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

def findSmallCaves(path):
    small_caves = [cave for cave in path if cave.lower() == cave]
    return small_caves

def findAllPaths(graph, start, end):
    paths = []
    stack = [[start]]
    while len(stack) > 0:
        visit_small = True
        path = stack.pop()
        current = path[-1]
        small_caves = findSmallCaves(path)
        for cave in small_caves:
            if small_caves.count(cave) > 1:
                visit_small = False

        if current == end:
            paths.append(path)
        else: 
            for neighbor in graph[current]:
                # if neighbor is a small cave visited once 
                # but there's no other small caves visited twice previously
                if  neighbor.lower() == neighbor and neighbor in path:
                    if visit_small and neighbor != start:
                        new_path = path.copy()
                        new_path.append(neighbor)
                        stack.append(new_path)
                # if neighbor is either a big cave, a small cave hasn't been visited or end
                if neighbor.lower() not in path:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    stack.append(new_path)
                
    # print(paths)
    return len(paths)


graph = makeGraph('input1212.txt')
paths = findAllPaths(graph, 'start', 'end')
print(paths)