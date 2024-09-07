"""Using for loop to ilutrate Big O: O(n)
"""
def print_items(n):
    # [print(i) for i in range(n)]
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)
