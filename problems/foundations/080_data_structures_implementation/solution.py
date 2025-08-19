"""
Solution for Data Structures Implementation
Problem ID: F080
"""

class Node:
    def __init__(self, data):
        # TODO: Implement your solution here
        pass

class LinkedList:
    def __init__(self):
        # TODO: Implement your solution here
        pass
    
    def append(self, data):
        # TODO: Implement your solution here
        pass
    
    def prepend(self, data):
        # TODO: Implement your solution here
        pass
    
    def delete(self, data):
        # TODO: Implement your solution here
        pass
    
    def find(self, data):
        # TODO: Implement your solution here
        pass
    
    def to_list(self):
        # TODO: Implement your solution here
        pass
    
    def __len__(self):
        # TODO: Implement your solution here
        pass

class HashTable:
    def __init__(self, size=10):
        # TODO: Implement your solution here
        pass
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
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
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(key)
    
    def delete(self, key):
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
