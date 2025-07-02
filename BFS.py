# ============================================
# Breadth-First Search (BFS)
# ============================================

# Define the graph as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# BFS function
def bfs(start_node):
    # Set to remember visited nodes
    visited = set()

    # List to act as our queue
    queue = []

    # Mark start node as visited
    visited.add(start_node)

    # Add start node to the queue
    queue.append(start_node)

    print("BFS traversal order:")

    # Loop until the queue is empty
    while queue:
        # Remove the first item in the queue
        node = queue.pop(0)

        # Process the node
        print(node)

        # For each neighbor of the current node
        for neighbor in graph[node]:
            # If neighbor hasn't been visited yet
            if neighbor not in visited:
                # Mark it visited
                visited.add(neighbor)

                # Add it to the queue to visit later
                queue.append(neighbor)

# Call BFS starting from node 'A'
bfs("A")
