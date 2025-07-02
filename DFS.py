# ============================================
# Depth-First Search (DFS) with User Input
# No recursion, using stack
# ============================================

#  Define the graph as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

#  DFS function
def dfs(start_node):
    # Set to keep track of visited nodes
    visited = set()

    # List to act as a stack
    stack = []

    # Add start node to the stack
    stack.append(start_node)

    print("\nDFS traversal order:")

    #  Loop until the stack is empty
    while stack:
        # Remove the last element (LIFO)
        node = stack.pop()

        # If node was not visited yet
        if node not in visited:
            # Mark as visited
            visited.add(node)

            # Process the node
            print(node)

            # Add neighbors to the stack (reverse order for consistency)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

#  Ask the user for the start node
start = input("Enter the start node (A-F): ").strip().upper()

#  Check if the start node exists in the graph
if start in graph:
    dfs(start)
else:
    print("Invalid node! Please enter a node between A and F.")
