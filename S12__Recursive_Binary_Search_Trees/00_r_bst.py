class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)
    

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
    The lines above create this tree
         2
        / \
        1   3
"""

print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value)
print('Root -> Right:', my_tree.root.right.value)
print('\n')


my_tree.delete_node(2)
"""
    The lines above create this tree
         3
        / \
        1   None
"""
print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value)
# print('Root -> Right:', my_tree.root.right.value)

# Create complete tree
# my_tree.r_insert(47)
# my_tree.r_insert(21)
# my_tree.r_insert(76)
# my_tree.r_insert(18)
# my_tree.r_insert(27)
# my_tree.r_insert(52)
# my_tree.r_insert(82)

# Test Contains
# print('BST Contains 27:')
# print(my_tree.r_contains(27))  # True

# print('BST contains 17:')
# print(my_tree.r_contains(17))  # False


# Test min value
# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right))

