class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.rigth is None:
                    temp.rigth = new_node
                    return True
                temp = temp.rigth

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.rigth
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(50)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.rigth.value)

print(my_tree.contains(27))
print(my_tree.contains(17))
