# string_ops.py
# Module with string-related functions

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def capitalize_words(s):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring spaces and case)"""
    clean = ''.join(s.split()).lower()
    return clean == clean[::-1]

def word_frequency(s):
    """Return a dictionary of word frequencies"""
    words = s.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(s):
    """Find the longest word in a string"""
    words = s.split()
    if not words:
        return ""
    return max(words, key=len)
