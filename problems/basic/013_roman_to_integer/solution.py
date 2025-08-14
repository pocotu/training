"""
Roman to Integer - LeetCode Problem #13
Problem ID: 013

Roman numerals are represented by seven different symbols.
Given a roman numeral, convert it to an integer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def roman_to_int(s):
    """
    Convert roman numeral string to integer.
    
    Args:
        s: Roman numeral string
        
    Returns:
        Integer value of roman numeral
    """
    # Mapping of roman numerals to integers
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Process string from right to left
    for char in reversed(s):
        value = roman_map[char]
        
        # If current value is less than previous, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

def roman_to_int_left_to_right(s):
    """
    Alternative solution processing left to right.
    
    Args:
        s: Roman numeral string
        
    Returns:
        Integer value of roman numeral
    """
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        # Check if current and next characters form a subtractive pair
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
    
    return total

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXC", 1994),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MCDXLIV", 1444)
    ]
    
    print("Testing Roman to Integer:")
    print("=" * 40)
    
    for roman, expected in test_cases:
        result1 = roman_to_int(roman)
        result2 = roman_to_int_left_to_right(roman)
        print(f"{roman:8} -> Expected: {expected:4}, Method1: {result1:4}, Method2: {result2:4}, Correct: {result1 == expected == result2}")
