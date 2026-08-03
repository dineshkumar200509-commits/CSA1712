from itertools import permutations

# Distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in permutations(vertices):
        current_cost = 0
        current_vertex = start

        for vertex in path:
            current_cost += graph[current_vertex][vertex]
            current_vertex = vertex

        current_cost += graph[current_vertex][start]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(path) + [start]

    print("Minimum Cost:", min_cost)
    print("Optimal Path:", " -> ".join(map(str, best_path)))

# Driver Code
travelling_salesman(graph, 0)