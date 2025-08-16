"""
Solution for Data Structures Implementation
Problem ID: F080
"""

class Node:
    """Node for linked list implementation."""
    
    def __init__(self, data):
        """Initialize node with data."""
        self.data = data
        self.next = None

class LinkedList:
    """
    Simple linked list implementation.
    """
    
    def __init__(self):
        """Initialize empty linked list."""
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add element to end of list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add element to beginning of list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, data):
        """Find data in list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def to_list(self):
        """Convert to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        """Return size of list."""
        return self.size

class HashTable:
    """
    Simple hash table implementation.
    """
    
    def __init__(self, size=10):
        """Initialize hash table with given size."""
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size
    
    def set(self, key, value):
        """Set key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
    
    def get(self, key):
        """Get value by key."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(key)
    
    def delete(self, key):
        """Delete key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(key)
    
    def keys(self):
        """Return all keys."""
        keys = []
        for bucket in self.table:
            for k, v in bucket:
                keys.append(k)
        return keys

def main():
    """
    Función principal para 080_data_structures_implementation
    """
    print("Data Structures Implementation Examples:")
    
    # Linked List
    print("\n1. Linked List:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    
    print(f"List: {ll.to_list()}")
    print(f"Size: {len(ll)}")
    print(f"Find 2: {ll.find(2)}")
    print(f"Find 5: {ll.find(5)}")
    
    ll.delete(2)
    print(f"After deleting 2: {ll.to_list()}")
    
    # Hash Table
    print("\n2. Hash Table:")
    ht = HashTable()
    ht.set("name", "Alice")
    ht.set("age", 25)
    ht.set("city", "New York")
    
    print(f"Name: {ht.get('name')}")
    print(f"Age: {ht.get('age')}")
    print(f"All keys: {ht.keys()}")
    
    ht.delete("age")
    print(f"Keys after deleting age: {ht.keys()}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")
