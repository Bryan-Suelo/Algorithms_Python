def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_streak = 0
    
    # Iterate through the set of numbers
    for num in num_set:
        # Only start counting from the beginning of a possible sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Check for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # Update the longest streak found
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


# Test case
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
