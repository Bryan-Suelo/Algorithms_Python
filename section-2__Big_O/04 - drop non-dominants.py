"""Using for loop to ilutrate Big O: O(n)
"""
def print_items(n):
    # For loop represents O(n^2)
    for i in range(n): 
        for j in range(n):
            print(i, j)

    # For loop represents O(n)
    for k in range(n):
        print(k)


print_items(10)
