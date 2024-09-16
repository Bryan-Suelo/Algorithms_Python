class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        # two or more items in list
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# Test if linked list is created correctly
# my_linked_list = LinkedList(4)
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print(my_linked_list.print_list())


# Test the append function
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# my_linked_list.print_list()
# print('\n')

# Test pop
# print(my_linked_list.pop())     # (2) Items - Returns 2 node
# print(my_linked_list.pop())     # (1) Items - Returns 1 node
# print(my_linked_list.pop())     # (0) Items - Returns None

# Test prepend
# my_linked_list.prepend(0)
# my_linked_list.print_list()

# Test pop first
# print(my_linked_list.pop_first())     # (2) Items - Returns 1 node
# print(my_linked_list.pop_first())     # (1) Items - Returns 2 node
# print(my_linked_list.pop_first())     # (0) Items - Returns None

# Test get
# print(my_linked_list.get(2))

# Test set_value
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# my_linked_list.set_value(1, 4)
# my_linked_list.print_list()  # Output: 11 -> 4 -> 23 -> 7

# Test insert
# my_linked_list.insert(1, 1)
# my_linked_list.print_list()  # Output: 11 -> 1 -> 23 ->

# Test remove
# print(my_linked_list.remove(2), '\n')
# my_linked_list.print_list()  # Output: 11 -> 23 -> 7

# Test reverse
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print('\n')

my_linked_list.reverse()
my_linked_list.print_list()  # Output: 4 -> 3 -> 2 ->
