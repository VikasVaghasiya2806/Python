# ===========================================
# Simple Dijkstra's Algorithm
# ===========================================

# Example graph as an adjacency list with weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Function to find the shortest paths from start_node
def dijkstra(graph, start_node):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0  # Distance to start node is 0

    # Track visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Select the unvisited node with the smallest distance
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node

        # No reachable remaining nodes
        if min_node is None:
            break

        # Visit neighbors and update their distances
        for neighbor, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        # Mark node as visited
        visited.add(min_node)

    return distances

# Example usage
start = 'A'
result = dijkstra(graph, start)

# Print the shortest distances
print(f"Shortest distances from node {start}:")
for node, distance in result.items():
    print(f"{node}: {distance}")
