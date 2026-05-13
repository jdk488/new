import heapq

# Goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Heuristic: Manhattan Distance
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal_state.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# Get neighbors by moving blank (0)
def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    x, y = divmod(i, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_i = nx * 3 + ny
            new_state = list(state)
            new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
            neighbors.append(tuple(new_state))

    return neighbors


def astar(start):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal_state:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            new_g = g_cost[current] + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    return None


# Initial state (0 = blank)
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = astar(start_state)

# Print solution
print("Steps to solve:")
for step in solution:
    for i in range(0, 9, 3):
        print(step[i:i+3])
    print()