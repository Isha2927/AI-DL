from collections import deque

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def is_goal(state):
    return state == GOAL_STATE


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(state_to_tuple(start))

    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path + [state]

        for neighbor in get_neighbors(state):
            t = state_to_tuple(neighbor)
            if t not in visited:
                visited.add(t)
                queue.append((neighbor, path + [state]))
    return None

def dfs(start, depth_limit=30):
    stack = [(start, [])]
    visited = set()
    visited.add(state_to_tuple(start))

    while stack:
        state, path = stack.pop()
        if is_goal(state):
            return path + [state]

        if len(path) >= depth_limit:
            continue

        for neighbor in get_neighbors(state):
            t = state_to_tuple(neighbor)
            if t not in visited:
                visited.add(t)
                stack.append((neighbor, path + [state]))
    return None

if __name__ == "__main__":
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("BFS Solution:")
    bfs_path = bfs(start_state)
    if bfs_path:
        for step in bfs_path:
            for row in step:
                print(row)
            print("---")
    else:
        print("No solution found with BFS")

    print("\nDFS Solution:")
    dfs_path = dfs(start_state)
    if dfs_path:
        for step in dfs_path:
            for row in step:
                print(row)
            print("---")
    else:
        print("No solution found with DFS")
