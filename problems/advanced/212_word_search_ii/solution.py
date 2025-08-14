"""
Solution for Word Search II
Problem ID: 212
LeetCode Problem: https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, 
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""

class TrieNode:
    """Trie node for efficient word storage and prefix checking."""
    
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at end nodes
        self.is_word = False

class WordSearchII:
    """
    Optimized solution using Trie + DFS backtracking.
    
    Time Complexity: O(M*N*4^L) where M*N is board size, L is max word length
    Space Complexity: O(K*L) where K is number of words, L is average length
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.result = set()
        self.board = []
        self.rows = 0
        self.cols = 0
    
    def build_trie(self, words: list[str]) -> None:
        """Build trie from word list."""
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            node.is_word = True
    
    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Main function to find all words in the board."""
        if not board or not board[0] or not words:
            return []
        
        self.board = board
        self.rows, self.cols = len(board), len(board[0])
        self.result = set()
        
        # Build trie for efficient prefix checking
        self.build_trie(words)
        
        # Try starting from each cell
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] in self.root.children:
                    self.dfs(i, j, self.root)
        
        return list(self.result)
    
    def dfs(self, row: int, col: int, node: TrieNode) -> None:
        """DFS with backtracking to find words."""
        # Get current character
        char = self.board[row][col]
        current_node = node.children[char]
        
        # Check if we found a word
        if current_node.is_word:
            self.result.add(current_node.word)
        
        # Mark current cell as visited
        self.board[row][col] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < self.rows and 
                0 <= new_col < self.cols and 
                self.board[new_row][new_col] != '#' and
                self.board[new_row][new_col] in current_node.children):
                
                self.dfs(new_row, new_col, current_node)
        
        # Restore original character (backtrack)
        self.board[row][col] = char

class WordSearchIIOptimized:
    """
    Enhanced version with pruning optimizations.
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.result = set()
        self.board = []
        self.rows = 0
        self.cols = 0
    
    def build_trie(self, words: list[str]) -> None:
        """Build trie with word counting for pruning."""
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            node.is_word = True
    
    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Find all words with optimizations."""
        if not board or not board[0] or not words:
            return []
        
        self.board = board
        self.rows, self.cols = len(board), len(board[0])
        self.result = set()
        
        # Build trie
        self.build_trie(words)
        
        # Try starting from each cell
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] in self.root.children:
                    self.dfs_optimized(i, j, self.root)
        
        return list(self.result)
    
    def dfs_optimized(self, row: int, col: int, node: TrieNode) -> None:
        """DFS with pruning optimizations."""
        char = self.board[row][col]
        current_node = node.children[char]
        
        # Check if we found a word
        if current_node.is_word:
            self.result.add(current_node.word)
            # Optional: remove word from trie to avoid duplicates
            current_node.is_word = False
        
        # Pruning: if no more words can be formed, return early
        if not current_node.children:
            return
        
        # Mark as visited
        self.board[row][col] = '#'
        
        # Explore neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < self.rows and 
                0 <= new_col < self.cols and 
                self.board[new_row][new_col] != '#' and
                self.board[new_row][new_col] in current_node.children):
                
                self.dfs_optimized(new_row, new_col, current_node)
        
        # Backtrack
        self.board[row][col] = char

class WordSearchIINaive:
    """
    Naive approach using DFS for each word separately.
    Used for comparison and educational purposes.
    """
    
    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Find words using individual DFS for each word."""
        if not board or not board[0] or not words:
            return []
        
        self.board = board
        self.rows, self.cols = len(board), len(board[0])
        result = []
        
        for word in words:
            if self.exist(word):
                result.append(word)
        
        return result
    
    def exist(self, word: str) -> bool:
        """Check if word exists in board using DFS."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, word, 0):
                    return True
        return False
    
    def dfs(self, row: int, col: int, word: str, index: int) -> bool:
        """DFS to check if word can be formed starting from (row, col)."""
        if index == len(word):
            return True
        
        if (row < 0 or row >= self.rows or 
            col < 0 or col >= self.cols or 
            self.board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = self.board[row][col]
        self.board[row][col] = '#'
        
        # Try all 4 directions
        found = (self.dfs(row + 1, col, word, index + 1) or
                self.dfs(row - 1, col, word, index + 1) or
                self.dfs(row, col + 1, word, index + 1) or
                self.dfs(row, col - 1, word, index + 1))
        
        # Backtrack
        self.board[row][col] = temp
        
        return found

# Main function for the problem
def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Main solution using optimized Trie approach.
    """
    solver = WordSearchIIOptimized()
    return solver.find_words(board, words)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic case from LeetCode
        (
            [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]],
            ["oath","pea","eat","rain"],
            ["eat","oath"]
        ),
        
        # Single character words
        (
            [["a","b"],
             ["c","d"]],
            ["a","b","c","d","ab","cd","ac","bd"],
            ["a","b","c","d"]  # Only single chars exist
        ),
        
        # No words found
        (
            [["a","b"],
             ["c","d"]],
            ["xyz","abc"],
            []
        ),
        
        # All words found
        (
            [["a","b","c"],
             ["a","e","d"],
             ["a","f","g"]],
            ["abcdefg","bed","aed"],
            ["bed","aed"]
        ),
        
        # Long word
        (
            [["a","b","c","e"],
             ["s","f","c","s"],
             ["a","d","e","e"]],
            ["abcced","see","seed","aced"],
            ["abcced","see","seed"]
        ),
        
        # Single cell
        (
            [["a"]],
            ["a","aa"],
            ["a"]
        ),
        
        # Empty cases
        ([], ["word"], []),
        ([["a"]], [], []),
        
        # Duplicate words in input
        (
            [["a","b"],
             ["c","d"]],
            ["ab","ab","cd"],
            ["ab","cd"]  # Should not have duplicates in result
        ),
    ]
    
    print("=" * 60)
    print("WORD SEARCH II - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Naive DFS", WordSearchIINaive()),
        ("Trie + DFS", WordSearchII()),
        ("Optimized Trie", WordSearchIIOptimized()),
    ]
    
    for i, (board, words, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Board: {board}")
        print(f"  Words: {words}")
        print(f"  Expected: {sorted(expected)}")
        
        results = []
        for name, solver in algorithms:
            try:
                import time
                import copy
                
                # Create deep copy of board for each algorithm
                board_copy = copy.deepcopy(board)
                
                start_time = time.time()
                result = solver.find_words(board_copy, words)
                end_time = time.time()
                
                result_sorted = sorted(result)
                results.append(result_sorted)
                
                status = "✓" if result_sorted == sorted(expected) else "✗"
                print(f"  {name}: {result_sorted} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(tuple(r) for r in results)) > 1:
            print(f"  WARNING: Inconsistent results: {results}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import string
    import time
    
    def generate_random_board(rows, cols):
        """Generate random character board."""
        return [[random.choice(string.ascii_lowercase) 
                for _ in range(cols)] for _ in range(rows)]
    
    def generate_random_words(count, min_len=3, max_len=8):
        """Generate random words."""
        words = set()
        while len(words) < count:
            length = random.randint(min_len, max_len)
            word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
            words.add(word)
        return list(words)
    
    def plant_words_in_board(board, words, planted_count=3):
        """Plant some words in the board to ensure some matches."""
        rows, cols = len(board), len(board[0])
        planted = []
        
        for _ in range(min(planted_count, len(words))):
            word = random.choice(words)
            if len(word) > max(rows, cols):
                continue
            
            # Try to plant horizontally or vertically
            direction = random.choice(['horizontal', 'vertical'])
            
            if direction == 'horizontal' and len(word) <= cols:
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - len(word))
                for i, char in enumerate(word):
                    board[row][col + i] = char
                planted.append(word)
            
            elif direction == 'vertical' and len(word) <= rows:
                row = random.randint(0, rows - len(word))
                col = random.randint(0, cols - 1)
                for i, char in enumerate(word):
                    board[row + i][col] = char
                planted.append(word)
        
        return planted
    
    performance_tests = [
        ("Small board", 4, 4, 10),
        ("Medium board", 6, 6, 20),
        ("Large board", 10, 10, 50),
        ("Wide board", 5, 15, 30),
        ("Tall board", 15, 5, 30),
    ]
    
    for test_name, rows, cols, word_count in performance_tests:
        print(f"\n{test_name} ({rows}x{cols}, {word_count} words):")
        
        # Generate test data
        board = generate_random_board(rows, cols)
        words = generate_random_words(word_count)
        
        # Plant some words to ensure matches
        planted = plant_words_in_board(board, words)
        print(f"  Planted words: {len(planted)}")
        
        # Test algorithms (skip naive for large cases)
        test_algorithms = algorithms if rows * cols <= 36 else algorithms[1:]
        
        results = []
        for name, solver in test_algorithms:
            try:
                import copy
                board_copy = copy.deepcopy(board)
                
                start_time = time.time()
                result = solver.find_words(board_copy, words)
                end_time = time.time()
                
                results.append(len(result))
                print(f"  {name}: {len(result)} words found, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Verify consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Different word counts found: {results}")
    
    # Edge case testing
    print("\n" + "=" * 60)
    print("EDGE CASE TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("Single cell, single char word", [["a"]], ["a"]),
        ("Single cell, two char word", [["a"]], ["aa"]),
        ("2x2 board, diagonal word", [["a","b"],["c","d"]], ["ac","bd"]),
        ("All same character", [["a","a"],["a","a"]], ["a","aa","aaa"]),
        ("Very long word", [["a"]*10], ["a"*15]),
        ("Empty word list", [["a","b"],["c","d"]], []),
        ("Word longer than board", [["a","b"]], ["abcdef"]),
        ("Repeated letters in word", [["a","b","a"],["b","a","b"]], ["aba","bab"]),
    ]
    
    for description, board, words in edge_cases:
        print(f"\n{description}:")
        print(f"  Board: {board}")
        print(f"  Words: {words}")
        
        # Test with optimized solver
        try:
            import copy
            solver = WordSearchIIOptimized()
            board_copy = copy.deepcopy(board)
            result = solver.find_words(board_copy, words)
            print(f"  Found: {result}")
            
        except Exception as e:
            print(f"  ERROR: {e}")
    
    # Memory usage analysis
    print("\n" + "=" * 60)
    print("MEMORY USAGE ANALYSIS")
    print("=" * 60)
    
    import sys
    
    def estimate_trie_memory(words):
        """Estimate memory usage of trie structure."""
        total_chars = sum(len(word) for word in words)
        unique_prefixes = len(set(word[:i] for word in words for i in range(1, len(word) + 1)))
        
        # Rough estimation: each node has dict + word storage
        estimated_nodes = min(total_chars, unique_prefixes)
        estimated_bytes = estimated_nodes * 100  # Rough estimate per node
        
        return estimated_bytes, estimated_nodes
    
    memory_test_cases = [
        (100, 5, "Many short words"),
        (50, 10, "Fewer long words"),
        (200, 7, "Large word list"),
    ]
    
    for word_count, avg_length, description in memory_test_cases:
        print(f"\n{description} ({word_count} words, avg length {avg_length}):")
        
        words = generate_random_words(word_count, avg_length - 2, avg_length + 2)
        estimated_bytes, estimated_nodes = estimate_trie_memory(words)
        estimated_mb = estimated_bytes / (1024 * 1024)
        
        print(f"  Estimated trie memory: ~{estimated_mb:.2f} MB")
        print(f"  Estimated nodes: ~{estimated_nodes}")
        print(f"  Memory per word: ~{estimated_bytes / word_count:.0f} bytes")
    
    # Algorithm complexity analysis
    print("\n" + "=" * 60)
    print("ALGORITHM COMPLEXITY ANALYSIS")
    print("=" * 60)
    
    def analyze_complexity(board_size, word_count, avg_word_length):
        """Analyze time complexity for different approaches."""
        m, n = board_size
        k = word_count
        l = avg_word_length
        
        # Naive approach: O(k * m * n * 4^l)
        naive_ops = k * m * n * (4 ** l)
        
        # Trie approach: O(m * n * 4^l) [worst case when all paths are explored]
        trie_ops = m * n * (4 ** l)
        
        # Space complexity
        trie_space = k * l  # Approximate
        
        return naive_ops, trie_ops, trie_space
    
    complexity_cases = [
        ((4, 4), 10, 5, "Small case"),
        ((6, 6), 20, 6, "Medium case"),
        ((10, 10), 50, 7, "Large case"),
    ]
    
    print("Time complexity estimates (operations):")
    for board_size, word_count, avg_length, description in complexity_cases:
        naive_ops, trie_ops, trie_space = analyze_complexity(board_size, word_count, avg_length)
        
        print(f"\n{description}:")
        print(f"  Board: {board_size[0]}x{board_size[1]}")
        print(f"  Words: {word_count} (avg length {avg_length})")
        print(f"  Naive approach: ~{naive_ops:,.0f} operations")
        print(f"  Trie approach: ~{trie_ops:,.0f} operations")
        print(f"  Speedup factor: ~{naive_ops / trie_ops:.1f}x")
        print(f"  Trie space: ~{trie_space} units")
    
    # Best practices summary
    print("\n" + "=" * 60)
    print("BEST PRACTICES SUMMARY")
    print("=" * 60)
    
    print("Algorithm Choice:")
    print("  • Use Trie + DFS for multiple word search")
    print("  • Naive DFS only for single word or very few words")
    print("  • Optimized Trie with pruning for production use")
    
    print("\nOptimization Techniques:")
    print("  • Build Trie once, use for all searches")
    print("  • Prune Trie branches after finding words")
    print("  • Early termination when no more children exist")
    print("  • Mark cells as visited during DFS, restore on backtrack")
    
    print("\nTime Complexity:")
    print("  • Naive: O(k * m * n * 4^l) - k words, m*n board, l avg length")
    print("  • Trie: O(m * n * 4^l) - independent of word count")
    print("  • Space: O(k * l) for Trie storage")
    
    print("\nWhen to Use:")
    print("  • Many words: Always use Trie approach")
    print("  • Few words (< 5): Consider naive approach for simplicity")
    print("  • Large board: Use optimized version with pruning")
    print("  • Memory constrained: Consider word-by-word processing")
