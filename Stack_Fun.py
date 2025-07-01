# Create an empty list to use as the stack
stack = []

# Function to push an element onto the stack
def push(element):
    stack.append(element)
    print(f"Pushed: {element}")

# Function to pop an element from the stack
def pop():
    if is_empty():
        print("Stack is empty! Cannot pop.")
    else:
        removed = stack.pop()
        print(f"Popped: {removed}")

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Example usage
push("Apple")
push("Banana")
push("Cherry")

print("Stack now:", stack)

pop()
pop()

print("Is stack empty?", is_empty())

pop()
pop()  # Try popping from empty stack

print("Final stack:", stack)
