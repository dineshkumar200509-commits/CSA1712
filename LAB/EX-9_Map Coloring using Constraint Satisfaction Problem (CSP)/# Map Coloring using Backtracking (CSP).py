# Map Coloring using Backtracking (CSP)

# Graph representing neighboring states
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store assigned colors
solution = {}

def is_safe(state, color):
    for neighbor in graph[state]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def map_coloring(states, index):
    if index == len(states):
        return True

    state = states[index]

    for color in colors:
        if is_safe(state, color):
            solution[state] = color

            if map_coloring(states, index + 1):
                return True

            del solution[state]

    return False

# Driver Code
states = list(graph.keys())

if map_coloring(states, 0):
    print("Map Coloring Solution:")
    for state in states:
        print(state, "->", solution[state])
else:
    print("No solution exists.")