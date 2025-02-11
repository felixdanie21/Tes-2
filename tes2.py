def custom_sort(arr):
    letters = sorted([x for x in arr if isinstance(x, str)])
    numbers = sorted([x for x in arr if isinstance(x, int)])
    return letters + numbers

arr = [12,9,30,"A","M",99,82,"J","N","B"]
print(custom_sort(arr))  # Output: ['A', 'B', 'J', 'M', 'N', 9, 12, 30, 82, 99]

def pattern_count(text, pattern):
    if not pattern:
        return 0
    
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(pattern_count("palindrom", "ind"))  # Output: 1
print(pattern_count("abakadabra", "ab"))  # Output: 2
print(pattern_count("hello", ""))  # Output: 0
print(pattern_count("ababab", "aba"))  # Output: 2
print(pattern_count("aaaaaa", "aa"))  # Output: 5
print(pattern_count("hell", "hello"))  # Output: 0

def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    return dict(sorted(letter_count.items()))

print(count_letters("Hello World"))  # Output: {'H': 1, 'W': 1, 'd': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1}
print(count_letters("Bismillah"))  # Output: {'B': 1, 'a': 1, 'h': 1, 'i': 2, 'l': 2, 'm': 1, 's': 1}
print(count_letters("MasyaAllah"))  # Output: {'A': 1, 'M': 1, 'a': 3, 'h': 1, 'l': 2, 's': 1, 'y': 1}
