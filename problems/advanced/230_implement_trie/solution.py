"""
Solution for Implement Trie (Prefix Tree)
Problem ID: 208
LeetCode Problem: https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.
"""

class TrieNode:
    """Basic Trie node implementation."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Basic Trie implementation with dictionary-based children.
    
    Time Complexities:
    - Insert: O(m) where m is the key length
    - Search: O(m) where m is the key length
    - StartsWith: O(m) where m is the prefix length
    
    Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of keys, M is average length
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class TrieNodeArray:
    """Trie node using array for children (optimized for lowercase letters)."""
    
    def __init__(self):
        self.children = [None] * 26  # for 'a' to 'z'
        self.is_end_of_word = False

class TrieOptimized:
    """
    Optimized Trie implementation using arrays for children.
    More memory efficient for specific alphabets.
    
    Time Complexities: Same as basic Trie
    Space Complexity: O(26 * N * M) - more predictable memory usage
    """
    
    def __init__(self):
        self.root = TrieNodeArray()
    
    def _char_to_index(self, char: str) -> int:
        """Convert character to array index."""
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if node.children[index] is None:
                node.children[index] = TrieNodeArray()
            node = node.children[index]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            index = self._char_to_index(char)
            if node.children[index] is None:
                return False
            node = node.children[index]
        return True

class TrieCompressed:
    """
    Compressed Trie (Radix Tree) implementation.
    Compresses chains of single-child nodes.
    """
    
    def __init__(self):
        self.root = {'children': {}, 'is_end': False, 'prefix': ''}
    
    def insert(self, word: str) -> None:
        """Insert a word into the compressed trie."""
        self._insert_helper(self.root, word, 0)
    
    def _insert_helper(self, node, word, start):
        """Helper function for insertion."""
        if start == len(word):
            node['is_end'] = True
            return
        
        char = word[start]
        
        if char not in node['children']:
            # Create new node with remaining suffix
            new_node = {
                'children': {},
                'is_end': True,
                'prefix': word[start:]
            }
            node['children'][char] = new_node
            return
        
        child = node['children'][char]
        prefix = child['prefix']
        
        # Find common prefix
        i = 0
        while (i < len(prefix) and 
               start + i < len(word) and 
               prefix[i] == word[start + i]):
            i += 1
        
        if i == len(prefix):
            # Prefix matches completely, continue with child
            self._insert_helper(child, word, start + i)
        else:
            # Split the node
            # Create new intermediate node
            old_child = {
                'children': child['children'],
                'is_end': child['is_end'],
                'prefix': prefix[i:]
            }
            
            # Update current child
            child['children'] = {prefix[i]: old_child}
            child['is_end'] = (start + i == len(word))
            child['prefix'] = prefix[:i]
            
            # Add remaining part if needed
            if start + i < len(word):
                remaining = word[start + i:]
                new_node = {
                    'children': {},
                    'is_end': True,
                    'prefix': remaining[1:]  # Skip first char (already in children key)
                }
                child['children'][remaining[0]] = new_node
    
    def search(self, word: str) -> bool:
        """Search for a word in the compressed trie."""
        return self._search_helper(self.root, word, 0)
    
    def _search_helper(self, node, word, start):
        """Helper function for search."""
        if start == len(word):
            return node['is_end']
        
        char = word[start]
        if char not in node['children']:
            return False
        
        child = node['children'][char]
        prefix = child['prefix']
        
        # Check if word matches the prefix
        if start + len(prefix) > len(word):
            return False
        
        for i, p_char in enumerate(prefix):
            if word[start + i] != p_char:
                return False
        
        return self._search_helper(child, word, start + len(prefix))
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word starts with the given prefix."""
        return self._starts_with_helper(self.root, prefix, 0)
    
    def _starts_with_helper(self, node, prefix, start):
        """Helper function for prefix search."""
        if start == len(prefix):
            return True
        
        char = prefix[start]
        if char not in node['children']:
            return False
        
        child = node['children'][char]
        node_prefix = child['prefix']
        
        # Check how much of the prefix matches
        i = 0
        while (i < len(node_prefix) and 
               start + i < len(prefix) and 
               node_prefix[i] == prefix[start + i]):
            i += 1
        
        if start + i >= len(prefix):
            return True  # Prefix fully matched
        
        if i < len(node_prefix):
            return False  # Partial match with node prefix
        
        return self._starts_with_helper(child, prefix, start + i)

# Additional utility functions for advanced Trie operations
class TrieAdvanced(Trie):
    """
    Advanced Trie with additional operations.
    """
    
    def delete(self, word: str) -> bool:
        """Delete a word from the trie."""
        return self._delete_helper(self.root, word, 0)
    
    def _delete_helper(self, node, word, index):
        """Helper function for deletion."""
        if index == len(word):
            if not node.is_end_of_word:
                return False  # Word doesn't exist
            
            node.is_end_of_word = False
            # Return True if node has no children (can be deleted)
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False  # Word doesn't exist
        
        child_node = node.children[char]
        should_delete_child = self._delete_helper(child_node, word, index + 1)
        
        if should_delete_child:
            del node.children[char]
            # Return True if current node can be deleted
            return not node.is_end_of_word and len(node.children) == 0
        
        return False
    
    def get_all_words(self) -> list[str]:
        """Get all words in the trie."""
        words = []
        self._collect_words(self.root, "", words)
        return words
    
    def _collect_words(self, node, prefix, words):
        """Helper function to collect all words."""
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)
    
    def get_words_with_prefix(self, prefix: str) -> list[str]:
        """Get all words that start with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._collect_words(node, prefix, words)
        return words
    
    def count_words(self) -> int:
        """Count total number of words in the trie."""
        return self._count_words_helper(self.root)
    
    def _count_words_helper(self, node):
        """Helper function to count words."""
        count = 1 if node.is_end_of_word else 0
        for child in node.children.values():
            count += self._count_words_helper(child)
        return count

if __name__ == "__main__":
    # Test all Trie implementations
    print("=" * 60)
    print("TRIE IMPLEMENTATIONS - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    implementations = [
        ("Basic Trie", Trie),
        ("Optimized Trie (Array)", TrieOptimized),
        ("Compressed Trie", TrieCompressed),
        ("Advanced Trie", TrieAdvanced),
    ]
    
    # Test words
    test_words = ["apple", "app", "apricot", "banana", "band", "bandana", "can", "cat"]
    test_searches = ["app", "apple", "appl", "banana", "ban", "xyz", ""]
    test_prefixes = ["app", "ban", "ca", "xyz", ""]
    
    for name, trie_class in implementations:
        print(f"\nTesting {name}:")
        print("-" * 40)
        
        try:
            trie = trie_class()
            
            # Insert words
            print("Inserting words:", test_words)
            for word in test_words:
                trie.insert(word)
            
            # Test search
            print("\nSearch results:")
            for word in test_searches:
                result = trie.search(word)
                print(f"  search('{word}'): {result}")
            
            # Test prefix search
            print("\nPrefix search results:")
            for prefix in test_prefixes:
                result = trie.startsWith(prefix)
                print(f"  startsWith('{prefix}'): {result}")
            
            # Test advanced operations if available
            if hasattr(trie, 'get_all_words'):
                words = trie.get_all_words()
                print(f"\nAll words in trie: {sorted(words)}")
                
                word_count = trie.count_words()
                print(f"Total word count: {word_count}")
                
                # Test prefix word collection
                prefix_words = trie.get_words_with_prefix("app")
                print(f"Words with prefix 'app': {sorted(prefix_words)}")
                
                # Test deletion
                print(f"\nDeleting 'app': {trie.delete('app')}")
                print(f"Search 'app' after deletion: {trie.search('app')}")
                print(f"Search 'apple' after deletion: {trie.search('apple')}")
            
        except Exception as e:
            print(f"  ERROR: {e}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import time
    import random
    import string
    
    def generate_random_words(count, min_len=3, max_len=10):
        """Generate random words for testing."""
        words = []
        for _ in range(count):
            length = random.randint(min_len, max_len)
            word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
            words.append(word)
        return words
    
    test_sizes = [1000, 5000, 10000]
    
    for size in test_sizes:
        print(f"\nTesting with {size} words:")
        words = generate_random_words(size)
        
        for name, trie_class in implementations[:3]:  # Skip advanced for large tests
            try:
                # Measure insertion time
                start_time = time.time()
                trie = trie_class()
                for word in words:
                    trie.insert(word)
                insert_time = time.time() - start_time
                
                # Measure search time
                search_words = random.sample(words, min(100, len(words)))
                start_time = time.time()
                for word in search_words:
                    trie.search(word)
                search_time = time.time() - start_time
                
                # Measure prefix search time
                prefixes = [word[:len(word)//2] for word in search_words]
                start_time = time.time()
                for prefix in prefixes:
                    trie.startsWith(prefix)
                prefix_time = time.time() - start_time
                
                print(f"  {name}:")
                print(f"    Insert {size} words: {insert_time:.4f}s")
                print(f"    Search 100 words: {search_time:.4f}s")
                print(f"    Prefix search 100: {prefix_time:.4f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Memory usage comparison
    print("\n" + "=" * 60)
    print("MEMORY USAGE TESTING")
    print("=" * 60)
    
    import sys
    
    def get_trie_size(trie, visited=None):
        """Estimate trie memory usage."""
        if visited is None:
            visited = set()
        
        if id(trie) in visited:
            return 0
        visited.add(id(trie))
        
        size = sys.getsizeof(trie)
        
        if hasattr(trie, 'root'):
            size += get_node_size(trie.root, visited)
        elif hasattr(trie, 'children'):
            size += get_node_size(trie, visited)
        
        return size
    
    def get_node_size(node, visited):
        """Estimate node memory usage."""
        if id(node) in visited:
            return 0
        visited.add(id(node))
        
        size = sys.getsizeof(node)
        
        if hasattr(node, 'children'):
            size += sys.getsizeof(node.children)
            if isinstance(node.children, dict):
                for child in node.children.values():
                    if child:
                        size += get_node_size(child, visited)
            elif isinstance(node.children, list):
                for child in node.children:
                    if child:
                        size += get_node_size(child, visited)
        
        return size
    
    # Test memory usage with same words
    test_words_mem = ["apple", "app", "application", "apply", "banana", "band", "bandana"]
    
    for name, trie_class in implementations[:3]:
        try:
            trie = trie_class()
            for word in test_words_mem:
                trie.insert(word)
            
            size = get_trie_size(trie)
            print(f"{name}: ~{size} bytes for {len(test_words_mem)} words")
            
        except Exception as e:
            print(f"{name}: ERROR - {e}")
    
    # Edge case testing
    print("\n" + "=" * 60)
    print("EDGE CASE TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("Empty string", ""),
        ("Single character", "a"),
        ("Long word", "a" * 1000),
        ("Repeated characters", "aaaa"),
        ("All alphabet", "abcdefghijklmnopqrstuvwxyz"),
    ]
    
    for description, word in edge_cases:
        print(f"\nTesting {description}: '{word[:20]}{'...' if len(word) > 20 else ''}'")
        
        for name, trie_class in implementations[:2]:  # Test main implementations
            try:
                trie = trie_class()
                trie.insert(word)
                
                search_result = trie.search(word)
                prefix_result = trie.startsWith(word[:len(word)//2] if word else "")
                
                print(f"  {name}: insert/search={search_result}, prefix={'✓' if prefix_result else '✗'}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
