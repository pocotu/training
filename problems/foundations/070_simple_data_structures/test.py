"""
Test cases for Simple Data Structures (Problem F070)
"""

import pytest
from solution import SimpleStack, SimpleQueue

class TestSimpleStack:
    
    def test_empty_stack(self):
        """Test empty stack operations"""
        stack = SimpleStack()
        assert stack.is_empty() == True
        assert stack.size() == 0
        assert stack.pop() == None
        assert stack.peek() == None
    
    def test_push_and_peek(self):
        """Test push and peek operations"""
        stack = SimpleStack()
        stack.push(1)
        assert stack.peek() == 1
        assert stack.size() == 1
        assert stack.is_empty() == False
        
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2
    
    def test_pop_operations(self):
        """Test pop operations"""
        stack = SimpleStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3
        assert stack.size() == 2
        assert stack.peek() == 2
        
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() == True
    
    def test_lifo_behavior(self):
        """Test LIFO (Last In, First Out) behavior"""
        stack = SimpleStack()
        items = [1, 2, 3, 4, 5]
        
        for item in items:
            stack.push(item)
        
        result = []
        while not stack.is_empty():
            result.append(stack.pop())
        
        assert result == [5, 4, 3, 2, 1]  # Reversed order


class TestSimpleQueue:
    
    def test_empty_queue(self):
        """Test empty queue operations"""
        queue = SimpleQueue()
        assert queue.is_empty() == True
        assert queue.size() == 0
        assert queue.dequeue() == None
        assert queue.front() == None
    
    def test_enqueue_and_front(self):
        """Test enqueue and front operations"""
        queue = SimpleQueue()
        queue.enqueue(1)
        assert queue.front() == 1
        assert queue.size() == 1
        assert queue.is_empty() == False
        
        queue.enqueue(2)
        assert queue.front() == 1  # Still first element
        assert queue.size() == 2
    
    def test_dequeue_operations(self):
        """Test dequeue operations"""
        queue = SimpleQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.dequeue() == 1
        assert queue.size() == 2
        assert queue.front() == 2
        
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty() == True
    
    def test_fifo_behavior(self):
        """Test FIFO (First In, First Out) behavior"""
        queue = SimpleQueue()
        items = [1, 2, 3, 4, 5]
        
        for item in items:
            queue.enqueue(item)
        
        result = []
        while not queue.is_empty():
            result.append(queue.dequeue())
        
        assert result == [1, 2, 3, 4, 5]  # Same order


class TestDataStructuresIntegration:
    
    def test_mixed_operations(self):
        """Test mixed operations on both structures"""
        stack = SimpleStack()
        queue = SimpleQueue()
        
        # Add same elements to both
        for i in range(3):
            stack.push(i)
            queue.enqueue(i)
        
        # Stack gives reverse order
        stack_result = []
        while not stack.is_empty():
            stack_result.append(stack.pop())
        
        # Queue gives same order
        queue_result = []
        while not queue.is_empty():
            queue_result.append(queue.dequeue())
        
        assert stack_result == [2, 1, 0]
        assert queue_result == [0, 1, 2]
