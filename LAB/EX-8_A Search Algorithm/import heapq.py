import heapq

# Graph with heuristic values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, start, [start]))

    visited = set()

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue,
                               (new_f, new_g, neighbor, path + [neighbor]))

    print("No Path Found")

# Driver Code
a_star(graph, 'A', 'G')