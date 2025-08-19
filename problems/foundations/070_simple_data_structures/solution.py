"""
Solution for Simple Data Structures
Problem ID: F070
"""

class SimpleStack:
    def __init__(self):
        # TODO: Implement your solution here
        pass
    
    def push(self, item):
        # TODO: Implement your solution here
        pass
    
    def pop(self):
        # TODO: Implement your solution here
        pass
    
    def peek(self):
        # TODO: Implement your solution here
        pass
    
    def is_empty(self):
        # TODO: Implement your solution here
        pass
    
    def size(self):
        # TODO: Implement your solution here
        pass


class SimpleQueue:
    def __init__(self):
        # TODO: Implement your solution here
        pass
    
    def enqueue(self, item):
        # TODO: Implement your solution here
        pass
    
    def dequeue(self):
        # TODO: Implement your solution here
        pass
    
    def front(self):
        # TODO: Implement your solution here
        pass
    
    def is_empty(self):
        # TODO: Implement your solution here
        pass
    
    def size(self):
        # TODO: Implement your solution here
        pass


def main():
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
