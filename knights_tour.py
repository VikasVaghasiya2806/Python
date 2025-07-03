# ================================================
# Knight's Tour with Fixed Start and Goal
# Printing Only Start, Goal, Final State, and Nodes Explored
# ================================================

N = 5  # Board size

# All 8 knight moves
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Initialize empty board
def init_board():
    return [[-1 for _ in range(N)] for _ in range(N)]

# Check if a move is safe
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Print the board
def print_board(board):
    for row in board:
        for cell in row:
            if cell == -1:
                print(" .", end=" ")
            else:
                print(f"{cell:2}", end=" ")
        print()
    print()

# Backtracking function to find Knight's Tour
def solve_knight(x, y, move_count, board, goal_x, goal_y, nodes_explored):
    nodes_explored[0] += 1

    # If all squares are visited
    if move_count == N * N:
        return x == goal_x and y == goal_y

    for i in range(8):
        nx = x + move_x[i]
        ny = y + move_y[i]
        if is_safe(nx, ny, board):
            board[nx][ny] = move_count
            if solve_knight(nx, ny, move_count + 1, board, goal_x, goal_y, nodes_explored):
                return True
            board[nx][ny] = -1

    return False

# Main function
def knight_tour_fixed():
    board = init_board()

    # Fixed start and goal positions
    start_x, start_y = 0, 0
    goal_x, goal_y = 4, 4

    print("=" * 50)
    print(f"Knight's Tour on {N}x{N} Board")
    print(f"Start position: ({start_x}, {start_y})")
    print(f"Goal position : ({goal_x}, {goal_y})")
    print("=" * 50)
    print()

    # Mark starting cell
    board[start_x][start_y] = 0

    # Nodes explored counter
    nodes_explored = [0]

    if solve_knight(start_x, start_y, 1, board, goal_x, goal_y, nodes_explored):
        print("Tour FOUND!\n")
        print_board(board)
    else:
        print("No tour exists.\n")

    print(f"Total nodes explored: {nodes_explored[0]}")

# Run
if __name__ == "__main__":
    knight_tour_fixed()
