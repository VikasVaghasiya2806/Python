
# Create empty lists for stack and queue
stack = []
queue = []

print("=== STACK EXAMPLE ===")
# Push elements onto the stack
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack after pushing A, B, C:", stack)

# Pop elements from the stack (LIFO)
print("Pop from stack:", stack.pop())  # Removes C
print("Pop from stack:", stack.pop())  # Removes B
print("Stack after popping twice:", stack)


print("\n=== QUEUE EXAMPLE ===")
# Enqueue elements into the queue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueuing A, B, C:", queue)

# Dequeue elements from the queue (FIFO)
print("Dequeue from queue:", queue.pop(0))  # Removes A
print("Dequeue from queue:", queue.pop(0))  # Removes B
print("Queue after dequeuing twice:", queue)
