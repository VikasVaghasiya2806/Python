
# Create an empty list to use as the stack
stack = []

# Display a welcome message
print("Simple Stack Example")

# Push elements onto the stack
stack.append("First")
stack.append("Second")
stack.append("Third")

# Display the stack
print("Stack after pushing 3 elements:", stack)

# Pop elements from the stack
top_item = stack.pop()
print("Popped:", top_item)

# Display the stack after pop
print("Stack after popping 1 element:", stack)

# Push another element
stack.append("Fourth")
print("Stack after pushing 'Fourth':", stack)

# Pop all remaining elements
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())

# Show the empty stack
print("Stack is now empty:", stack)
