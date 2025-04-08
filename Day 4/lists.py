from collections import deque

stuff = []

stuff.append("hello")
stuff.append(123)
stuff.append(45.67)
stuff.append(True)
stuff.append(["a", "b", "c"])
stuff.append(None)
stuff.append({"key": "value"})

for item in stuff:
    print(item)

print()

stuff.insert(0, "world")

for item in stuff:
    print(item)

# Create a FIFO queue
fifo_queue = deque()

# Add elements to the queue
fifo_queue.append("first")
fifo_queue.append("second")
fifo_queue.append("third")

# Remove elements from the queue
while fifo_queue:
    print(fifo_queue.popleft())


