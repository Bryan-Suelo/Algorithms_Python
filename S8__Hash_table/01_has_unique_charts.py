def has_unique_chars(string):
    # Create a set to track characters
    seen_chars = set()
    
    # Iterate through the string
    for char in string:
        if char in seen_chars:  # If character is already in set, it's a duplicate
            return False
        seen_chars.add(char)  # Add the character to the set
    
    return True  # All characters are unique 




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False