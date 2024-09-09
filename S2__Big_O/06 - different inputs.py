"""Using for loop to ilutrate Big O: O(n)
"""
def print_items_v1(a, b):
    # The following inputs give O(a + b)
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

def print_items_v2(a, b):
    # The following inputs give O(a * b)
    for i in range(a):        
        for j in range(b):
            print(i, j)


print_items_v1(5, 6)
print_items_v2(5, 6)
