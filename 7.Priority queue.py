
# Create an empty list to hold (priority, item) pairs
priority_queue = []

# Add elements (priority, item)
priority_queue.append((2, "Task B"))
priority_queue.append((1, "Task A"))
priority_queue.append((3, "Task C"))

# Sort the list by priority (lowest priority number first)
priority_queue.sort()

# Display the queue
print("Priority Queue:", priority_queue)

# Pop elements in priority order
first = priority_queue.pop(0)
print("Popped:", first)

second = priority_queue.pop(0)
print("Popped:", second)

third = priority_queue.pop(0)
print("Popped:", third)

print("Priority Queue:", priority_queue)
