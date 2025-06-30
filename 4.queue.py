# Create an empty list to use as the queue
queue = []

# Display a welcome message
print("Simple Queue Example")

# Enqueue elements (add elements to the queue)
queue.append("First")
queue.append("Second")
queue.append("Third")

# Display the queue
print("Queue after enqueuing 3 elements:", queue)

# Dequeue elements (remove elements from the front)
first_item = queue.pop(0)
print("Dequeued:", first_item)

# Display the queue after dequeue
print("Queue after dequeuing 1 element:", queue)

# Enqueue another element
queue.append("Fourth")
print("Queue after enqueuing 'Fourth':", queue)

# Dequeue all remaining elements
second_item = queue.pop(0)
print("Dequeued:", second_item)

third_item = queue.pop(0)
print("Dequeued:", third_item)

fourth_item = queue.pop(0)
print("Dequeued:", fourth_item)

# Show the empty queue
print("Queue is now empty:", queue)
