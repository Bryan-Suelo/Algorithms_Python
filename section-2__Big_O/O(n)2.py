"""Using for loop to ilutrate Big O: O(n)
"""
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(10)
