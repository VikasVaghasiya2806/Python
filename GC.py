from collections import deque

# Each state is a tuple:
# (Farmer side, Wolf side, Goat side, Cabbage side)
# Each side is 'L' (left) or 'R' (right)

# Define the initial state
start_state = ('L', 'L', 'L', 'L')

# Define the goal state
goal_state = ('R', 'R', 'R', 'R')

# Helper: opposite side
def opposite(side):
    return 'R' if side == 'L' else 'L'

# Function to check whether a state is safe
def is_safe(state):
    _, wolf, goat, cabbage = state
    # Goat and Cabbage alone
    if goat == cabbage and state[0] != goat:
        return False
    # Wolf and Goat alone
    if wolf == goat and state[0] != goat:
        return False
    return True

# Function to generate successors with move descriptions
def get_successors(state):
    successors = []
    farmer_side = state[0]

    # List to hold all attempted moves (for debug)
    attempted = []

    # Move alone
    next_state = (opposite(farmer_side), state[1], state[2], state[3])
    attempted.append(("Farmer moves alone", next_state))

    # Try moving each item
    items = ["Wolf", "Goat", "Cabbage"]
    for i in range(1, 4):
        if state[i] == farmer_side:
            new_state = list(state)
            new_side = opposite(farmer_side)
            new_state[0] = new_side
            new_state[i] = new_side
            attempted.append((f"Farmer takes {items[i-1]}", tuple(new_state)))

    # Now check which are safe and collect
    for desc, s in attempted:
        if is_safe(s):
            successors.append((s, desc))
        else:
            print(f"INVALID move: {desc} --> Unsafe configuration.")

    return successors

# BFS to find shortest path
def bfs(start, goal):
    queue = deque()
    queue.append((start, [start], []))  # (state, path, actions)
    visited = set()
    visited.add(start)
    nodes_explored = 0

    while queue:
        current_state, path, actions = queue.popleft()
        nodes_explored += 1

        if current_state == goal:
            return path, actions, nodes_explored

        for successor, desc in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor], actions + [desc]))

    return None, None, nodes_explored

# Function to pretty-print a state visually
def print_state(state):
    left = []
    right = []
    names = ["Farmer", "Wolf", "Goat", "Cabbage"]
    for i, side in enumerate(state):
        if side == 'L':
            left.append(names[i])
        else:
            right.append(names[i])
    print(f"Left bank: {', '.join(left) if left else '---'}")
    print(f"Right bank: {', '.join(right) if right else '---'}")
    print()

# Main function
def main():
    print("Solving the Goat, Wolf, Cabbage Problem...")
    path, actions, nodes_explored = bfs(start_state, goal_state)

    print(f"\nTotal nodes explored: {nodes_explored}\n")

    if path:
        print(f"Solution found in {len(path) - 1} moves:\n")
        for i, state in enumerate(path):
            print(f"Step {i}:")
            if i == 0:
                print("Start state.")
            else:
                print(f"Action: {actions[i-1]}")
            print_state(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
