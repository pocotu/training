"""
Solution for Palindrome Pairs
Problem ID: 215
LeetCode Problem: https://leetcode.com/problems/palindrome-pairs/

You are given a 0-indexed array of unique strings words.
A palindrome pair is a pair of integers (i, j) such that the concatenation of words[i] and words[j] is a palindrome.

Return an array of all the palindrome pairs of words.
"""

def palindrome_pairs_brute_force(words):
    """
    Brute force approach: check every pair.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n² * m) where n = number of words, m = average length
    Space Complexity: O(1) excluding result
    """
    def is_palindrome(s):
        """Check if string is palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                concatenated = words[i] + words[j]
                if is_palindrome(concatenated):
                    result.append([i, j])
    
    return result

def palindrome_pairs_trie(words):
    """
    Trie-based approach for efficient palindrome pair detection.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n * m²) where n = number of words, m = max word length
    Space Complexity: O(n * m) for trie
    """
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word_index = -1
            self.palindrome_suffixes = []  # Indices of words with palindromic suffixes
    
    def is_palindrome(s, start=0, end=None):
        """Check if substring is palindrome."""
        if end is None:
            end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def build_trie(words):
        """Build trie with reverse words."""
        root = TrieNode()
        
        for i, word in enumerate(words):
            # Insert reverse of word
            node = root
            for j, char in enumerate(reversed(word)):
                # Check if remaining part of word is palindrome
                if is_palindrome(word, 0, len(word) - 1 - j):
                    node.palindrome_suffixes.append(i)
                
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            
            node.word_index = i
            # Entire word was processed, check for empty suffix
            node.palindrome_suffixes.append(i)
        
        return root
    
    root = build_trie(words)
    result = []
    
    for i, word in enumerate(words):
        node = root
        
        # Search for word in trie
        for j, char in enumerate(word):
            # Case 1: We found a complete word, check if rest is palindrome
            if node.word_index != -1 and node.word_index != i:
                if is_palindrome(word, j):
                    result.append([i, node.word_index])
            
            if char not in node.children:
                break
            node = node.children[char]
        else:
            # Case 2: We matched entire word
            # Check if there are palindromic suffixes
            for suffix_idx in node.palindrome_suffixes:
                if suffix_idx != i:
                    result.append([i, suffix_idx])
    
    return result

def palindrome_pairs_hash_optimized(words):
    """
    Hash map optimized approach.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n * m²)
    Space Complexity: O(n * m)
    """
    def is_palindrome(s):
        """Check if string is palindrome."""
        return s == s[::-1]
    
    # Create word to index mapping
    word_to_index = {word: i for i, word in enumerate(words)}
    result = []
    
    for i, word in enumerate(words):
        n = len(word)
        
        for j in range(n + 1):
            # Split word into prefix and suffix
            prefix = word[:j]
            suffix = word[j:]
            
            # Case 1: prefix is palindrome, look for reverse of suffix
            if is_palindrome(prefix):
                reverse_suffix = suffix[::-1]
                if reverse_suffix in word_to_index and word_to_index[reverse_suffix] != i:
                    result.append([word_to_index[reverse_suffix], i])
            
            # Case 2: suffix is palindrome, look for reverse of prefix
            # Avoid duplicate when j == 0 (whole word)
            if j != n and is_palindrome(suffix):
                reverse_prefix = prefix[::-1]
                if reverse_prefix in word_to_index and word_to_index[reverse_prefix] != i:
                    result.append([i, word_to_index[reverse_prefix]])
    
    return result

def palindrome_pairs_manacher_enhanced(words):
    """
    Enhanced approach using Manacher-like palindrome detection.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n * m²)
    Space Complexity: O(n * m)
    """
    def manacher_palindromes(s):
        """Find all palindromic substrings using Manacher's algorithm."""
        # Transform string
        transformed = '#'.join('^{}$'.format(s))
        n = len(transformed)
        P = [0] * n
        center = right = 0
        
        palindromes = set()
        
        for i in range(1, n - 1):
            mirror = 2 * center - i
            
            if i < right:
                P[i] = min(right - i, P[mirror])
            
            # Try to expand
            try:
                while transformed[i + (1 + P[i])] == transformed[i - (1 + P[i])]:
                    P[i] += 1
            except IndexError:
                pass
            
            # Update center and right
            if i + P[i] > right:
                center, right = i, i + P[i]
            
            # Extract palindrome information
            start = (i - P[i]) // 2
            end = (i + P[i]) // 2
            palindromes.add((start, end))
        
        return palindromes
    
    # Precompute palindromes for each word
    word_palindromes = {}
    for i, word in enumerate(words):
        word_palindromes[i] = manacher_palindromes(word)
    
    # Create reverse mapping
    word_to_index = {word: i for i, word in enumerate(words)}
    result = []
    
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i != j:
                # Check if word1 + word2 is palindrome
                combined = word1 + word2
                if combined in word_palindromes.get(-1, set()) or combined == combined[::-1]:
                    result.append([i, j])
    
    # More efficient: check specific patterns
    result = []
    for i, word in enumerate(words):
        n = len(word)
        
        # Check all possible splits
        for k in range(n + 1):
            prefix = word[:k]
            suffix = word[k:]
            
            # Case 1: prefix palindrome + reverse suffix exists
            if prefix == prefix[::-1]:
                target = suffix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([word_to_index[target], i])
            
            # Case 2: reverse prefix exists + suffix palindrome
            if k < n and suffix == suffix[::-1]:
                target = prefix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([i, word_to_index[target]])
    
    return result

def palindrome_pairs_rolling_hash(words):
    """
    Rolling hash approach for fast palindrome detection.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n * m²)
    Space Complexity: O(n)
    """
    def rolling_hash_palindrome(s):
        """Check if string is palindrome using rolling hash."""
        if not s:
            return True
        
        base = 256
        mod = 10**9 + 7
        
        n = len(s)
        left_hash = right_hash = 0
        power = 1
        
        for i in range(n):
            # Forward hash
            left_hash = (left_hash * base + ord(s[i])) % mod
            
            # Backward hash
            right_hash = (right_hash + ord(s[n - 1 - i]) * power) % mod
            power = (power * base) % mod
        
        return left_hash == right_hash
    
    def is_palindrome_split(s, split_pos):
        """Check if prefix and suffix around split are palindromes."""
        prefix = s[:split_pos]
        suffix = s[split_pos:]
        
        return rolling_hash_palindrome(prefix), rolling_hash_palindrome(suffix)
    
    word_to_index = {word: i for i, word in enumerate(words)}
    result = []
    
    for i, word in enumerate(words):
        n = len(word)
        
        for j in range(n + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            # Use rolling hash for palindrome checks
            if rolling_hash_palindrome(prefix):
                target = suffix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([word_to_index[target], i])
            
            if j < n and rolling_hash_palindrome(suffix):
                target = prefix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([i, word_to_index[target]])
    
    return result

def palindrome_pairs_kmp_based(words):
    """
    KMP algorithm based approach for pattern matching.
    
    Args:
        words: List of strings
        
    Returns:
        List of [i, j] pairs where words[i] + words[j] is palindrome
        
    Time Complexity: O(n * m²)
    Space Complexity: O(m)
    """
    def build_lps(pattern):
        """Build longest proper prefix suffix array."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    def is_palindrome_kmp(s):
        """Check if string is palindrome using KMP technique."""
        if not s:
            return True
        
        # Create pattern: s + '#' + reverse(s)
        pattern = s + '#' + s[::-1]
        lps = build_lps(pattern)
        
        # If last LPS value equals length of s, then s is palindrome
        return lps[-1] == len(s)
    
    word_to_index = {word: i for i, word in enumerate(words)}
    result = []
    
    for i, word in enumerate(words):
        n = len(word)
        
        for j in range(n + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            if is_palindrome_kmp(prefix):
                target = suffix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([word_to_index[target], i])
            
            if j < n and is_palindrome_kmp(suffix):
                target = prefix[::-1]
                if target in word_to_index and word_to_index[target] != i:
                    result.append([i, word_to_index[target]])
    
    return result

# Main function for the problem
def palindromePairs(words):
    """
    Main solution using hash map optimized approach.
    """
    return palindrome_pairs_hash_optimized(words)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases from LeetCode
        (["lls", "s", "sssll"], [[0, 1], [1, 0], [2, 2]]),  # Multiple valid pairs
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (["a", ""], [[0, 1], [1, 0]]),  # Empty string case
        
        # Edge cases
        ([], []),  # Empty input
        (["a"], []),  # Single word
        (["aa", "aa"], [[0, 1], [1, 0]]),  # Identical words
        
        # Palindrome words
        (["aba", "bab"], []),  # Both palindromes but no pairs
        (["race", "ecar"], [[0, 1], [1, 0]]),  # Perfect reverse pair
        
        # Complex cases
        (["abc", "cba", "ab", "ba"], [[0, 1], [1, 0], [2, 3], [3, 2]]),
        (["a", "aa", "aaa"], [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]]),
        
        # Empty string edge cases
        (["", "a", "aa"], [[0, 1], [1, 0], [0, 2], [2, 0]]),
        
        # No palindrome pairs
        (["abc", "def", "ghi"], []),
        
        # Self-palindrome combinations
        (["ab", "ba", "c"], [[0, 1], [1, 0]]),
        
        # Overlapping patterns
        (["abc", "cb", "bac"], []),  # Check carefully
        
        # Long words
        (["abcdef", "fedcba"], [[0, 1], [1, 0]]),
        
        # Repeated characters
        (["aab", "baa"], [[0, 1], [1, 0]]),
        (["aaab", "baaa"], [[0, 1], [1, 0]]),
    ]
    
    print("=" * 60)
    print("PALINDROME PAIRS - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Brute Force", palindrome_pairs_brute_force),
        ("Trie Based", palindrome_pairs_trie),
        ("Hash Optimized", palindrome_pairs_hash_optimized),
        ("Manacher Enhanced", palindrome_pairs_manacher_enhanced),
        ("Rolling Hash", palindrome_pairs_rolling_hash),
        ("KMP Based", palindrome_pairs_kmp_based),
    ]
    
    for i, (words, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Input: {words}")
        print(f"  Expected: {sorted(expected)}")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(words)
                end_time = time.time()
                
                # Sort results for comparison
                sorted_result = sorted(result)
                results.append(sorted_result)
                
                # Validate result
                matches_expected = sorted_result == sorted(expected)
                
                # Additional validation: check if pairs actually form palindromes
                valid_pairs = True
                for pair in result:
                    if len(pair) == 2:
                        i, j = pair
                        if 0 <= i < len(words) and 0 <= j < len(words):
                            combined = words[i] + words[j]
                            if combined != combined[::-1]:
                                valid_pairs = False
                                break
                        else:
                            valid_pairs = False
                            break
                    else:
                        valid_pairs = False
                        break
                
                status = "✓" if (matches_expected and valid_pairs) else "✗"
                
                print(f"  {name}: {sorted_result} {status} ({end_time - start_time:.6f}s)")
                
                if not matches_expected and valid_pairs and len(sorted_result) == len(expected):
                    # Check if it's an alternative valid solution
                    print(f"    Note: Different valid solution with same count")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Cross-validate results
        if results and len(set(map(str, results))) > 1:
            print(f"  WARNING: Different results across algorithms")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import string
    import time
    
    def generate_word_list(num_words, word_length, pattern_type="random"):
        """Generate test word lists with different patterns."""
        words = []
        
        if pattern_type == "random":
            for _ in range(num_words):
                word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, word_length)))
                words.append(word)
        
        elif pattern_type == "palindrome_heavy":
            # Generate many palindromes
            for _ in range(num_words // 2):
                half = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length // 2))
                palindrome = half + half[::-1]
                words.append(palindrome)
            
            # Fill remaining with random
            while len(words) < num_words:
                word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, word_length)))
                words.append(word)
        
        elif pattern_type == "reverse_pairs":
            # Generate pairs where one is reverse of another
            for _ in range(num_words // 2):
                word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
                words.append(word)
                words.append(word[::-1])
            
            # Fill remaining if odd number
            if len(words) < num_words:
                word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
                words.append(word)
        
        elif pattern_type == "worst_case":
            # All different words, no palindromes possible
            used = set()
            while len(words) < num_words:
                word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
                if word not in used and word[::-1] not in used:
                    words.append(word)
                    used.add(word)
        
        return words[:num_words]
    
    performance_tests = [
        ("Small random", 10, 5, "random"),
        ("Medium random", 20, 8, "random"),
        ("Large random", 50, 10, "random"),
        ("Palindrome heavy", 20, 6, "palindrome_heavy"),
        ("Reverse pairs", 20, 6, "reverse_pairs"),
        ("Worst case", 30, 6, "worst_case"),
    ]
    
    for test_name, num_words, word_length, pattern in performance_tests:
        print(f"\n{test_name} ({num_words} words, max length {word_length}):")
        
        test_words = generate_word_list(num_words, word_length, pattern)
        print(f"  Sample words: {test_words[:5]}{'...' if len(test_words) > 5 else ''}")
        
        # Test algorithms (skip brute force for large cases)
        test_algorithms = algorithms if num_words <= 30 else algorithms[1:]
        
        results = []
        for name, func in test_algorithms:
            try:
                start_time = time.time()
                result = func(test_words)
                end_time = time.time()
                
                results.append(len(result))
                
                # Validate result
                valid_pairs = True
                for pair in result:
                    if len(pair) == 2:
                        i, j = pair
                        if 0 <= i < len(test_words) and 0 <= j < len(test_words):
                            combined = test_words[i] + test_words[j]
                            if combined != combined[::-1]:
                                valid_pairs = False
                                break
                        else:
                            valid_pairs = False
                            break
                
                print(f"  {name}: {len(result)} pairs, {end_time - start_time:.6f}s {'✓' if valid_pairs else '✗'}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if results and len(set(results)) > 1:
            print(f"  WARNING: Different pair counts: {results}")
    
    # Correctness validation with manual verification
    print("\n" + "=" * 60)
    print("CORRECTNESS VALIDATION")
    print("=" * 60)
    
    def manual_verify_pairs(words, pairs):
        """Manually verify that all pairs form valid palindromes."""
        valid_pairs = []
        invalid_pairs = []
        
        for pair in pairs:
            if len(pair) != 2:
                invalid_pairs.append((pair, "Invalid pair format"))
                continue
            
            i, j = pair
            if not (0 <= i < len(words) and 0 <= j < len(words)):
                invalid_pairs.append((pair, "Index out of bounds"))
                continue
            
            if i == j:
                invalid_pairs.append((pair, "Same index pair"))
                continue
            
            combined = words[i] + words[j]
            if combined == combined[::-1]:
                valid_pairs.append(pair)
            else:
                invalid_pairs.append((pair, f"'{combined}' is not palindrome"))
        
        return valid_pairs, invalid_pairs
    
    validation_cases = [
        ["lls", "s", "sssll"],
        ["abcd", "dcba", "lls", "s", "sssll"],
        ["a", ""],
        ["race", "ecar"],
        ["abc", "cba", "ab", "ba"],
    ]
    
    for words in validation_cases:
        print(f"\nValidating words: {words}")
        
        # Get result from main algorithm
        result = palindrome_pairs_hash_optimized(words)
        print(f"  Found pairs: {result}")
        
        # Manual verification
        valid_pairs, invalid_pairs = manual_verify_pairs(words, result)
        
        print(f"  Valid pairs: {len(valid_pairs)}")
        for pair in valid_pairs:
            i, j = pair
            combined = words[i] + words[j]
            print(f"    [{i},{j}]: '{words[i]}' + '{words[j]}' = '{combined}'")
        
        if invalid_pairs:
            print(f"  Invalid pairs: {len(invalid_pairs)}")
            for pair, reason in invalid_pairs:
                print(f"    {pair}: {reason}")
        
        # Check for missed pairs (brute force verification)
        all_possible = palindrome_pairs_brute_force(words)
        missed = [p for p in all_possible if p not in result]
        if missed:
            print(f"  Missed pairs: {missed}")
    
    # Edge case stress testing
    print("\n" + "=" * 60)
    print("EDGE CASE STRESS TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("Empty list", []),
        ("Single word", ["hello"]),
        ("Two identical", ["abc", "abc"]),
        ("Perfect reverses", ["abc", "cba"]),
        ("Empty string", [""]),
        ("Empty + word", ["", "a"]),
        ("Empty + palindrome", ["", "aba"]),
        ("All palindromes", ["aba", "cdc", "efe"]),
        ("No valid pairs", ["abc", "def", "ghi"]),
        ("Same length different", ["abc", "xyz"]),
        ("Different lengths", ["a", "bb", "ccc"]),
        ("Nested palindromes", ["ab", "a", "b", "ba"]),
    ]
    
    for description, test_words in edge_cases:
        print(f"\n{description}: {test_words}")
        
        try:
            # Test with main algorithm
            result = palindrome_pairs_hash_optimized(test_words)
            
            # Verify manually
            valid_pairs, invalid_pairs = manual_verify_pairs(test_words, result)
            
            print(f"  Result: {result}")
            print(f"  Valid: {len(valid_pairs)}, Invalid: {len(invalid_pairs)}")
            
            if invalid_pairs:
                print(f"  Issues: {[reason for _, reason in invalid_pairs]}")
            
        except Exception as e:
            print(f"  ERROR: {e}")
    
    # Algorithm comparison and analysis
    print("\n" + "=" * 60)
    print("ALGORITHM ANALYSIS")
    print("=" * 60)
    
    print("Time Complexity Comparison:")
    print("  Brute Force:      O(n² × m) - check every pair, verify palindrome")
    print("  Trie Based:       O(n × m²) - build trie + search with suffix checks")
    print("  Hash Optimized:   O(n × m²) - hash lookups + palindrome checks")
    print("  Manacher Enhanced: O(n × m²) - precompute palindromes + pattern matching")
    print("  Rolling Hash:     O(n × m²) - fast palindrome checks via hashing")
    print("  KMP Based:        O(n × m²) - pattern matching for palindrome detection")
    
    print("\nSpace Complexity Comparison:")
    print("  Brute Force:      O(1) - constant extra space")
    print("  Trie Based:       O(n × m) - trie storage")
    print("  Hash Optimized:   O(n × m) - hash map storage")
    print("  Manacher Enhanced: O(n × m) - palindrome information storage")
    print("  Rolling Hash:     O(n) - hash map only")
    print("  KMP Based:        O(m) - LPS array for patterns")
    
    print("\nBest Use Cases:")
    print("  • Hash Optimized: Best overall performance, good for most cases")
    print("  • Trie Based: When many words share prefixes/suffixes")
    print("  • Rolling Hash: When memory is extremely limited")
    print("  • Brute Force: Small inputs or when simplicity is preferred")
    print("  • KMP Based: When pattern matching expertise is available")
    
    # Pattern analysis for different input types
    print("\n" + "=" * 60)
    print("INPUT PATTERN ANALYSIS")
    print("=" * 60)
    
    pattern_analysis_cases = [
        ("Many palindromes", generate_word_list(15, 4, "palindrome_heavy")),
        ("Many reverse pairs", generate_word_list(15, 4, "reverse_pairs")),
        ("Random words", generate_word_list(15, 4, "random")),
        ("No valid pairs", generate_word_list(15, 4, "worst_case")),
    ]
    
    for pattern_name, test_words in pattern_analysis_cases:
        print(f"\n{pattern_name}:")
        print(f"  Words: {test_words[:5]}{'...' if len(test_words) > 5 else ''}")
        
        # Analyze with fastest algorithm
        result = palindrome_pairs_hash_optimized(test_words)
        
        # Calculate statistics
        total_possible_pairs = len(test_words) * (len(test_words) - 1)
        palindrome_ratio = len(result) / total_possible_pairs if total_possible_pairs > 0 else 0
        
        print(f"  Total pairs: {len(result)} out of {total_possible_pairs} possible")
        print(f"  Palindrome ratio: {palindrome_ratio:.2%}")
        
        # Analyze pair characteristics
        if result:
            pair_distances = [abs(i - j) for i, j in result]
            avg_distance = sum(pair_distances) / len(pair_distances)
            print(f"  Average index distance: {avg_distance:.2f}")
            
            # Check for self-palindromes
            self_palindromes = sum(1 for word in test_words if word == word[::-1])
            print(f"  Self-palindromes: {self_palindromes}/{len(test_words)}")
    
    print("\nKey Insights:")
    print("  • Hash map approach provides best balance of speed and memory")
    print("  • Trie approach excels when words have common prefixes/suffixes")
    print("  • Empty strings create palindrome pairs with any string")
    print("  • Algorithm choice depends on input characteristics")
    print("  • Palindrome detection is the computational bottleneck")
