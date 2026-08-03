from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return (0 <= m_left <= 3) and (0 <= c_left <= 3)

def get_next_states(state):
    m_left, c_left, boat = state
    moves = [(2,0), (0,2), (1,1), (1,0), (0,1)]
    next_states = []

    for m, c in moves:
        if boat == 1:  # Boat on left side
            new_state = (m_left - m, c_left - c, 0)
        else:          # Boat on right side
            new_state = (m_left + m, c_left + c, 1)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution Path:")
            for step in path:
                print(step)
            return

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    print("No Solution Found")

solve()