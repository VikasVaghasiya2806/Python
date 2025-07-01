
# Define the size of the queue
SIZE = 5

# Create an empty list of fixed size
queue = [None] * SIZE

# Initialize front and rear pointers
front = -1
rear = -1

# Function to add an element (enqueue)
def enqueue(element):
    global rear, front
    if (rear + 1) % SIZE == front:
        print("Queue is Full!")
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % SIZE
        queue[rear] = element
        print(f"Enqueued: {element}")

# Function to remove an element (dequeue)
def dequeue():
    global rear, front
    if front == -1:
        print("Queue is Empty!")
    else:
        removed = queue[front]
        if front == rear:
            # Queue has only one element
            front = -1
            rear = -1
        else:
            front = (front + 1) % SIZE
        print(f"Dequeued: {removed}")

# Example usage:
enqueue("A")
enqueue("B")
enqueue("C")
enqueue("D")
enqueue("E")  # Should show "Queue is Full" after this

dequeue()
dequeue()

enqueue("F")
enqueue("G")  # Should fill up the queue again

print("Queue state:", queue)
