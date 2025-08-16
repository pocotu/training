"""
Solution for Simple Data Structures
Problem ID: F070
"""

class SimpleStack:
    """
    A simple stack implementation using a list.
    """
    
    def __init__(self):
        """Initialize empty stack."""
        self.items = []
    
    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item from stack."""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack."""
        return len(self.items)


class SimpleQueue:
    """
    A simple queue implementation using a list.
    """
    
    def __init__(self):
        """Initialize empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item from queue."""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in queue."""
        return len(self.items)


def main():
    """
    Función principal para 070_simple_data_structures
    """
    # Test Stack
    print("Testing Stack:")
    stack = SimpleStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Stack size: {stack.size()}")
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size after pops: {stack.size()}")
    
    # Test Queue
    print("\nTesting Queue:")
    queue = SimpleQueue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    
    print(f"Queue size: {queue.size()}")
    print(f"Front: {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Size after dequeues: {queue.size()}")
    
    return stack

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")
