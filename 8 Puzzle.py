from collections import deque
import random


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def get_successors(node):
    """
    Generate all valid successor states by moving the blank (0).
    """
    successors = []
    index = node.state.index(0)
    quotient = index // 3
    remainder = index % 3

    # Determine valid moves based on row
    if quotient == 0:
        moves = [3]          # can move down
    elif quotient == 1:
        moves = [-3, 3]      # can move up or down
    else:  # quotient == 2
        moves = [-3]         # can move up

    # Add moves based on column
    if remainder == 0:
        moves += [1]         # can move right
    elif remainder == 1:
        moves += [-1, 1]     # can move left or right
    else:  # remainder == 2
        moves += [-1]        # can move left

    # Generate new states for all valid moves
    for move in moves:
        im = index + move
        if 0 <= im < 9:
            new_state = list(node.state)
            new_state[index], new_state[im] = new_state[im], new_state[index]
            successors.append(Node(new_state, node))
    return successors

def bfs(start_state, goal_state):
    """
    Breadth-First Search to find the shortest sequence of moves from start to goal.
    """
    start_node = Node(start_state)
    goal_node = Node(goal_state)
    queue = deque([start_node])
    visited = set()
    nodes_explored = 0

    while queue:
        node = queue.popleft()
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        nodes_explored += 1

        if node.state == goal_node.state:
            # Reconstruct path from start to goal
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            print('Total nodes explored:', nodes_explored)
            return path[::-1]

        for successor in get_successors(node):
            queue.append(successor)

    return None

# Goal state: Solved configuration
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Randomly generate a start state by applying D random moves from the goal
s_node = Node(goal_state)
D = 20
d = 0
while d <= D:
    start_state = random.choice(get_successors(s_node)).state
    s_node = Node(start_state)
    d += 1

print("Random start state generated:")
for i in range(0, 9, 3):
    print(start_state[i:i+3])

# Solve the puzzle
solution = bfs(start_state, goal_state)

if solution:
    print("\nSolution found:")
    for step_num, step in enumerate(solution):
        print(f"Step {step_num}:")
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")
