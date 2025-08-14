"""
Solution for Add and Search Word - Data Structure Design
Problem ID: 211
LeetCode Problem: https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports adding new words and finding if a string matches any previously added word.
Implement the WordDictionary class with addWord and search methods.
The search method should support '.' as a wildcard that matches any letter.
"""

class TrieNode:
    """Trie node for word dictionary."""
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    """
    Word dictionary with wildcard search support.
    
    Operations:
    - addWord: O(m) where m is word length
    - search: O(m) for exact match, O(n * 26^k) for wildcards where k is number of '.' chars
    
    Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Add a word to the data structure."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for a word, supporting '.' as wildcard."""
        return self._search_helper(word, 0, self.root)
    
    def _search_helper(self, word: str, index: int, node: TrieNode) -> bool:
        """Recursive helper for search with wildcard support."""
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._search_helper(word, index + 1, child):
                    return True
            return False
        else:
            # Exact character match
            if char not in node.children:
                return False
            return self._search_helper(word, index + 1, node.children[char])

class WordDictionaryOptimized:
    """
    Optimized version with array-based children for lowercase letters.
    """
    
    class TrieNodeArray:
        def __init__(self):
            self.children = [None] * 26  # for 'a' to 'z'
            self.is_end_of_word = False
    
    def __init__(self):
        self.root = self.TrieNodeArray()
    
    def _char_to_index(self, char: str) -> int:
        """Convert character to array index."""
        return ord(char) - ord('a')
    
    def addWord(self, word: str) -> None:
        """Add a word to the data structure."""
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if node.children[index] is None:
                node.children[index] = self.TrieNodeArray()
            node = node.children[index]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for a word, supporting '.' as wildcard."""
        return self._search_helper(word, 0, self.root)
    
    def _search_helper(self, word: str, index: int, node) -> bool:
        """Recursive helper for search with wildcard support."""
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all non-None children
            for child in node.children:
                if child is not None and self._search_helper(word, index + 1, child):
                    return True
            return False
        else:
            # Exact character match
            child_index = self._char_to_index(char)
            if node.children[child_index] is None:
                return False
            return self._search_helper(word, index + 1, node.children[child_index])

class WordDictionaryIterative:
    """
    Iterative implementation to avoid recursion stack overflow.
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Add a word to the data structure."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Iterative search for a word with wildcard support."""
        # Stack contains tuples of (node, word_index)
        stack = [(self.root, 0)]
        
        while stack:
            node, index = stack.pop()
            
            if index == len(word):
                if node.is_end_of_word:
                    return True
                continue
            
            char = word[index]
            
            if char == '.':
                # Add all children to stack
                for child in node.children.values():
                    stack.append((child, index + 1))
            else:
                # Add specific child if exists
                if char in node.children:
                    stack.append((node.children[char], index + 1))
        
        return False

class WordDictionaryWithStats:
    """
    Enhanced version with statistics and additional operations.
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
        self.total_chars = 0
    
    def addWord(self, word: str) -> None:
        """Add a word to the data structure."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.word_count += 1
            self.total_chars += len(word)
    
    def search(self, word: str) -> bool:
        """Search for a word, supporting '.' as wildcard."""
        return self._search_helper(word, 0, self.root)
    
    def _search_helper(self, word: str, index: int, node: TrieNode) -> bool:
        """Recursive helper for search with wildcard support."""
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            for child in node.children.values():
                if self._search_helper(word, index + 1, child):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._search_helper(word, index + 1, node.children[char])
    
    def get_words_count(self) -> int:
        """Get total number of words."""
        return self.word_count
    
    def get_average_length(self) -> float:
        """Get average word length."""
        return self.total_chars / self.word_count if self.word_count > 0 else 0
    
    def get_all_words(self) -> list[str]:
        """Get all words in the dictionary."""
        words = []
        self._collect_words(self.root, "", words)
        return words
    
    def _collect_words(self, node: TrieNode, prefix: str, words: list[str]) -> None:
        """Helper to collect all words."""
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)
    
    def get_words_with_pattern(self, pattern: str) -> list[str]:
        """Get all words matching a pattern with wildcards."""
        result = []
        self._find_pattern_words(self.root, pattern, 0, "", result)
        return result
    
    def _find_pattern_words(self, node: TrieNode, pattern: str, index: int, current: str, result: list[str]) -> None:
        """Helper to find words matching pattern."""
        if index == len(pattern):
            if node.is_end_of_word:
                result.append(current)
            return
        
        char = pattern[index]
        
        if char == '.':
            for c, child in node.children.items():
                self._find_pattern_words(child, pattern, index + 1, current + c, result)
        else:
            if char in node.children:
                self._find_pattern_words(node.children[char], pattern, index + 1, current + char, result)

if __name__ == "__main__":
    # Test all implementations
    print("=" * 60)
    print("WORD DICTIONARY - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    implementations = [
        ("Basic Trie", WordDictionary),
        ("Optimized Array", WordDictionaryOptimized),
        ("Iterative", WordDictionaryIterative),
        ("With Statistics", WordDictionaryWithStats),
    ]
    
    # Test operations
    test_operations = [
        ("add", "bad"),
        ("add", "dad"),
        ("add", "mad"),
        ("search", "pad"),       # False
        ("search", "bad"),       # True
        ("search", ".ad"),       # True (matches bad, dad, mad)
        ("search", "b.."),       # True (matches bad)
        ("add", "fade"),
        ("search", "f.de"),      # True (matches fade)
        ("search", "f..e"),      # True (matches fade)
        ("search", "f..."),      # True (matches fade)
        ("search", "f...."),     # False (fade is only 4 chars)
        ("search", "...."),      # True (matches fade)
        ("search", "....."),     # False (no 5-char words)
    ]
    
    for name, dict_class in implementations:
        print(f"\nTesting {name}:")
        print("-" * 40)
        
        try:
            wd = dict_class()
            
            for operation, word in test_operations:
                if operation == "add":
                    wd.addWord(word)
                    print(f"  addWord('{word}')")
                elif operation == "search":
                    result = wd.search(word)
                    print(f"  search('{word}'): {result}")
            
            # Test additional features if available
            if hasattr(wd, 'get_words_count'):
                print(f"  Total words: {wd.get_words_count()}")
                print(f"  Average length: {wd.get_average_length():.2f}")
                
                # Test pattern matching
                patterns = [".ad", "..de", "f..."]
                for pattern in patterns:
                    matches = wd.get_words_with_pattern(pattern)
                    print(f"  Pattern '{pattern}' matches: {matches}")
                
        except Exception as e:
            print(f"  ERROR: {e}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import time
    import random
    import string
    
    def generate_random_words(count, min_len=3, max_len=8):
        """Generate random words for testing."""
        words = set()
        while len(words) < count:
            length = random.randint(min_len, max_len)
            word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
            words.add(word)
        return list(words)
    
    def generate_wildcard_queries(words, query_count=100):
        """Generate wildcard queries based on existing words."""
        queries = []
        
        for _ in range(query_count):
            if words:
                # Pick a random word and add some wildcards
                word = random.choice(words)
                query = list(word)
                
                # Replace some characters with wildcards
                wildcard_count = random.randint(0, min(2, len(word)))
                positions = random.sample(range(len(word)), wildcard_count)
                
                for pos in positions:
                    query[pos] = '.'
                
                queries.append(''.join(query))
            else:
                # Generate random wildcard query
                length = random.randint(3, 8)
                query = []
                for _ in range(length):
                    if random.random() < 0.3:  # 30% chance of wildcard
                        query.append('.')
                    else:
                        query.append(random.choice(string.ascii_lowercase))
                queries.append(''.join(query))
        
        return queries
    
    performance_tests = [
        ("Small dataset", 100, 50),
        ("Medium dataset", 1000, 200),
        ("Large dataset", 5000, 500),
    ]
    
    for test_name, word_count, query_count in performance_tests:
        print(f"\n{test_name} ({word_count} words, {query_count} queries):")
        
        # Generate test data
        words = generate_random_words(word_count)
        exact_queries = random.sample(words, min(query_count // 2, len(words)))
        wildcard_queries = generate_wildcard_queries(words, query_count // 2)
        
        for name, dict_class in implementations:
            try:
                wd = dict_class()
                
                # Measure insertion time
                start_time = time.time()
                for word in words:
                    wd.addWord(word)
                insert_time = time.time() - start_time
                
                # Measure exact search time
                start_time = time.time()
                exact_results = []
                for query in exact_queries:
                    exact_results.append(wd.search(query))
                exact_time = time.time() - start_time
                
                # Measure wildcard search time
                start_time = time.time()
                wildcard_results = []
                for query in wildcard_queries:
                    wildcard_results.append(wd.search(query))
                wildcard_time = time.time() - start_time
                
                print(f"  {name}:")
                print(f"    Insert {word_count} words: {insert_time:.4f}s")
                print(f"    {len(exact_queries)} exact searches: {exact_time:.4f}s")
                print(f"    {len(wildcard_queries)} wildcard searches: {wildcard_time:.4f}s")
                print(f"    Exact hit rate: {sum(exact_results)}/{len(exact_results)}")
                print(f"    Wildcard hit rate: {sum(wildcard_results)}/{len(wildcard_results)}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Edge case testing
    print("\n" + "=" * 60)
    print("EDGE CASE TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("Empty word", ""),
        ("Single character", "a"),
        ("Single wildcard", "."),
        ("All wildcards", "...."),
        ("Long word", "a" * 50),
        ("Mixed case simulation", "AbCdEf"),  # Assuming lowercase conversion
        ("Numbers (if supported)", "123"),
        ("Special chars (if supported)", "a-b"),
    ]
    
    print("Testing edge cases with Basic Trie:")
    wd = WordDictionary()
    
    # Add some words first
    test_words = ["a", "ab", "abc", "abcd", "test", "testing"]
    for word in test_words:
        try:
            wd.addWord(word)
            print(f"  Added: '{word}'")
        except Exception as e:
            print(f"  Failed to add '{word}': {e}")
    
    # Test edge case searches
    for description, query in edge_cases:
        try:
            result = wd.search(query)
            print(f"  {description} ('{query}'): {result}")
        except Exception as e:
            print(f"  {description} ('{query}'): ERROR - {e}")
    
    # Memory usage analysis
    print("\n" + "=" * 60)
    print("MEMORY USAGE ANALYSIS")
    print("=" * 60)
    
    import sys
    
    def estimate_trie_memory(wd, num_words, avg_length):
        """Estimate memory usage of trie."""
        # Rough estimation based on structure
        if isinstance(wd, WordDictionaryOptimized):
            # Array-based: 26 * 8 bytes per node
            estimated_nodes = num_words * avg_length * 0.7  # Sharing factor
            return int(estimated_nodes * 26 * 8), "Array-based"
        else:
            # Dict-based: variable size per node
            estimated_nodes = num_words * avg_length * 0.7
            return int(estimated_nodes * 100), "Dictionary-based"  # Rough estimate
    
    memory_test_cases = [
        (100, 5, "Small dictionary"),
        (1000, 6, "Medium dictionary"),
        (10000, 7, "Large dictionary"),
    ]
    
    for num_words, avg_length, description in memory_test_cases:
        print(f"\n{description} ({num_words} words, avg length {avg_length}):")
        
        for name, dict_class in implementations[:2]:  # Test main implementations
            try:
                estimated_bytes, method = estimate_trie_memory(dict_class(), num_words, avg_length)
                estimated_mb = estimated_bytes / (1024 * 1024)
                print(f"  {name}: ~{estimated_mb:.2f} MB ({method})")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Wildcard complexity analysis
    print("\n" + "=" * 60)
    print("WILDCARD COMPLEXITY ANALYSIS")
    print("=" * 60)
    
    def analyze_wildcard_complexity(pattern):
        """Analyze the search complexity of a wildcard pattern."""
        wildcard_count = pattern.count('.')
        exact_count = len(pattern) - wildcard_count
        
        # Worst case: 26^wildcard_count paths to explore
        worst_case_paths = 26 ** wildcard_count
        
        return wildcard_count, exact_count, worst_case_paths
    
    complexity_patterns = [
        "abc",      # No wildcards
        ".bc",      # 1 wildcard
        "a.c",      # 1 wildcard (middle)
        "ab.",      # 1 wildcard (end)
        "..c",      # 2 wildcards
        "a..",      # 2 wildcards
        "...",      # 3 wildcards
        "....",     # 4 wildcards
        "a.b.c",    # 2 wildcards, non-consecutive
    ]
    
    print("Pattern complexity analysis:")
    for pattern in complexity_patterns:
        wildcards, exact, paths = analyze_wildcard_complexity(pattern)
        print(f"  '{pattern}': {wildcards} wildcards, {exact} exact chars, ~{paths} max paths")
    
    # Real-world usage simulation
    print("\n" + "=" * 60)
    print("REAL-WORLD USAGE SIMULATION")
    print("=" * 60)
    
    # Simulate a spell checker or autocomplete system
    common_words = [
        "the", "and", "for", "are", "but", "not", "you", "all", "can", "had",
        "her", "was", "one", "our", "out", "day", "get", "has", "him", "his",
        "how", "man", "new", "now", "old", "see", "two", "way", "who", "boy",
        "did", "its", "let", "put", "say", "she", "too", "use"
    ]
    
    print("Simulating spell checker with common words:")
    wd = WordDictionary()
    
    # Add common words
    for word in common_words:
        wd.addWord(word)
    
    # Test spell checking scenarios
    spell_check_tests = [
        ("Exact match", "the", True),
        ("Missing letter", "th.", True),   # Should find "the"
        ("Wrong letter", ".he", True),    # Should find "the", "she"
        ("Transposition", ".oy", True),   # Should find "boy"
        ("Common typo", "teh", False),    # No such word
        ("Partial word", "...", True),    # Should find 3-letter words
        ("Length check", ".....", False), # No 5-letter words in our set
    ]
    
    for description, query, expected_found in spell_check_tests:
        result = wd.search(query)
        status = "✓" if (result and expected_found) or (not result and not expected_found) else "?"
        print(f"  {description}: '{query}' -> {result} {status}")
    
    # Performance with realistic patterns
    print("\nPerformance with realistic wildcard patterns:")
    realistic_patterns = [
        "...",     # Find 3-letter words
        ".he",     # Words ending in "he"
        "a..",     # Words starting with "a"
        "..e",     # Words ending with "e"
        ".a.",     # Words with "a" in middle
    ]
    
    for pattern in realistic_patterns:
        start_time = time.time()
        result = wd.search(pattern)
        end_time = time.time()
        
        print(f"  Pattern '{pattern}': {result} ({end_time - start_time:.6f}s)")
    
    print("\nImplementation Summary:")
    print("  • Basic Trie: Most flexible, good for general use")
    print("  • Optimized Array: Better memory efficiency for lowercase letters")
    print("  • Iterative: Avoids recursion limit, good for deep patterns")
    print("  • With Statistics: Provides additional insights and operations")
    print("  • Wildcard search complexity grows exponentially with '.' count")
    print("  • Best suited for moderate wildcard usage (1-3 '.' characters)")
