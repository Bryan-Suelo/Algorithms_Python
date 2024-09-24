# Algorithms_Python

Author: Bryan-Suelo

Examples and information from courses will be cover here. Setup and installation will also be here for getting started.

[Course Content](https://www.udemy.com/course/data-structures-algorithms-python/?couponCode=SEPTSTACK24A)

## Section 2. Big O

### Big O: Intro

#### Time Complexity

Computational concept that measures the amount of time an algorithm takes to complete as a function of the length of the input. It provides a way to evaluate the efficiency of an algorithm, particularly in terms of how the execution time grows as the size of the input increases.

Time complexity is often expressed using Big O notation, which describes the upper limit of the running time. It provides a high-level understanding of the algorithm's performance.

#### Space Complexity

Space complexity refers to the amount of memory an algorithm uses in relation to the size of the input data. It is an important aspect of algorithm analysis, as it helps determine how efficiently an algorithm utilizes memory resources.

### Big O: Worst Case

- Best case scenario: Omega
- Average case scenario: Theta
- Worst case scenario: Omicron

### Big O: O(n)

O(n) denotes linear time complexity, which means that the time it takes to complete the algorithm increases linearly with the size of the input data.

#### Key Characteristics of O(n)

1. **Linear Growth**: 
   - In an O(n) algorithm, if the input size doubles, the time taken to execute the algorithm also approximately doubles. This is because each element in the input must be processed individually.
2. **Common Examples**:
   - **Linear Search**: Searching for an element in an unsorted list requires checking each element until the desired one is found, resulting in O(n) complexity.
   - **Iterating Through a List**: Any operation that involves going through each element of a list or array, such as summing the elements or finding the maximum value, typically has O(n) complexity.

#### Practical Implications

1. **Scalability**: Algorithms with O(n) complexity are generally efficient for moderate input sizes. However, as the input size grows significantly, the performance may still become a concern, especially compared to algorithms with better complexities (like O(log n) or O(1)).
2. **Real-World Applications**: Understanding O(n) is crucial for developers when designing algorithms, as it helps in making informed decisions about which algorithms to use based on the expected size of the input data.

### Big O: O(n²)

O(n²) indicates that the time complexity of an algorithm increases quadratically as the input size (n) increases.

#### Key Elements of O(n²)

1. **Quadratic Growth**:
   - In an algorithm with O(n²) complexity, the number of operations grows proportionally to the square of the input size. For example, if the input size doubles, the time taken by the algorithm increases by a factor of four.
2. **Nested Loops**:
   - O(n²) complexity often arises from algorithms that involve nested loops. For instance, if you have an outer loop that runs n times and an inner loop that also runs n times for each iteration of the outer loop, the total number of iterations becomes n * n, leading to O(n²).
3. **Performance Impact**:
   - While O(n²) algorithms may perform adequately for small input sizes, their performance can degrade significantly as the input size increases. This is particularly important in applications where efficiency is critical.
4. **Examples**:
   - Common algorithms with O(n²) complexity include bubble sort, selection sort, and insertion sort. These algorithms typically involve comparing each element with every other element.
5. **Simplification**:
   - In Big O notation, constant factors and lower-order terms are ignored. Thus, an algorithm that runs in time proportional to 3n² + 2n + 5 is simplified to O(n²) because the n² term dominates as n grows large.

### Big O: O(1)

O(1), also known as constant time complexity, indicates that the execution time of an algorithm remains constant regardless of the size of the input data.

#### Key Elements of O(1)

1. **Constant Time Complexity**:
   - An algorithm with O(1) complexity performs a fixed number of operations, meaning its execution time does not change with varying input sizes. For example, accessing an element in an array by its index is an O(1) operation because it takes the same amount of time regardless of the array's length.
2. **Independence from Input Size**:
   - O(1) operations are not affected by the size of the input. This makes them particularly efficient for tasks that involve single actions or direct access to data structures.
3. **Examples**:
   - Common examples of O(1) operations include:
     - Accessing an element in an array using its index.
     - Looking up a value in a hash table (assuming minimal collisions).
     - Performing basic arithmetic operations like addition or subtraction.
4. **Efficiency**:
   - O(1) algorithms are highly efficient and desirable in scenarios where performance is critical. They allow for quick data retrieval and manipulation without the overhead of iterating through larger datasets.
5. **Mathematical Representation**:
   - In formal terms, an algorithm is said to have O(1) complexity if there exists a constant *M* such that the time taken *T(n)* is less than or equal to *M* for all sufficiently large *n*.

### Big O: O(log n)

O(log n), known as logarithmic time complexity, indicates that the execution time of an algorithm increases logarithmically as the input size (n) increases. Associated with divide and conquer.

#### Key Elements of O(log n)

1. **Logarithmic Growth**:
   - In an O(log n) algorithm, the time complexity grows logarithmically, meaning that as the input size increases, the number of operations increases at a much slower rate. For example, doubling the input size results in only a small increase in the number of operations required.
2. **Dividing the Input**:
   - O(log n) complexity often arises in algorithms that repeatedly divide the problem space in half. A classic example is the binary search algorithm, which halves the search space with each iteration, allowing it to find an element in a sorted array efficiently. This characteristic of discarding half of the input at each step is what leads to logarithmic complexity.
3. **Efficiency**:
   - Algorithms with O(log n) complexity are highly efficient, especially for large datasets. They are preferred in scenarios where quick search and retrieval operations are necessary, such as in databases and search engines.
4. **Examples**:
   - Common algorithms with O(log n) complexity include:
     - Binary search: Searching for an element in a sorted array.
     - Operations on balanced binary search trees: Inserting, deleting, or searching for elements.
     - Heap operations: Inserting or removing elements from a heap data structure.
5. **Mathematical Representation**:
   - In formal terms, an algorithm is said to have O(log n) complexity if the number of operations required to complete the algorithm can be expressed as a logarithmic function of the input size. The base of the logarithm is typically 2, reflecting the binary nature of many algorithms that exhibit this complexity.

## Section 4. Linked List

### Overview

A linked list is a linear data structure that consists of a series of elements called nodes, where each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not store their elements in contiguous memory locations, allowing for dynamic memory allocation and efficient insertion and deletion of nodes.

### Key Characteristics

1. Node Structure:
   - Each node in a linked list typically contains two components:
     - Data: The value or information stored in the node.
     - Next Pointer: A reference to the next node in the list. The last node's next pointer points to null, indicating the end of the list.
2. Dynamic Size:
   - Linked lists can grow and shrink in size dynamically, making them more flexible than arrays, which have a fixed size determined at creation.
3. Types of Linked Lists:
   - **Singly Linked List**: Each node points to the next node, allowing traversal in one direction.
   - **Doubly Linked List**: Each node contains pointers to both the next and the previous nodes, enabling traversal in both directions.
   - **Circular Linked List**: The last node points back to the first node, forming a circle, which allows for continuous traversal.
4. Operations:
   - **Insertion**: Nodes can be added at the beginning, end, or any position within the list. This involves adjusting the pointers of the neighboring nodes.
   - **Deletion**: Removing a node requires updating the pointers of adjacent nodes to maintain the list's integrity.
   - **Searching**: To find a specific value, the list must be traversed from the head node until the value is found or the end of the list is reached.
5. Performance:
   - Accessing elements in a linked list is generally slower than in arrays because it requires sequential traversal from the head node to the desired node. This results in a linear time complexity of O(n) for search operations, while insertion and deletion can be performed in O(1) time if the position is known.

## Section 5. Doubly Linked List

### Overview of Doubly Linked Lists

A doubly linked list is a type of linked list in which each node contains three fields: two pointers (or references) and one data field. The two pointers allow for navigation in both directions—forward and backward—making it easier to traverse the list compared to a singly linked list.

### Key Characteristics of Doubly Linked Lists

1. **Node Structure**:
   - Each node in a doubly linked list consists of:
     - **Data**: The value or information stored in the node.
     - **Next Pointer**: A reference to the next node in the sequence.
     - **Previous Pointer**: A reference to the previous node in the sequence. This allows traversal in both directions.
2. **Bidirectional Traversal**:
   - The presence of both next and previous pointers enables traversal of the list in both forward and backward directions. This is particularly useful for certain applications where reverse traversal is needed.
3. **Dynamic Size**:
   - Like other linked lists, doubly linked lists can grow and shrink dynamically, allowing for efficient memory usage without the need for contiguous memory allocation.
4. **Operations**:
   - **Insertion**: Nodes can be added at the beginning, end, or any position within the list. Insertion involves adjusting the pointers of the neighboring nodes to maintain the list's integrity.
   - **Deletion**: Removing a node requires updating the pointers of both the next and previous nodes, ensuring that the list remains connected.
   - **Searching**: Similar to singly linked lists, searching for a specific value requires traversing the list, but can be done in either direction.
5. Performance:
   - Accessing elements in a doubly linked list is generally slower than in arrays due to the need for traversal. However, insertion and deletion operations can be performed in O(1) time if the position is known, as both pointers can be easily adjusted.

### Advantages and Disadvantages of Doubly Linked Lists

1. **Advantages**:
   - **Bidirectional Traversal**: The ability to traverse in both directions simplifies certain operations and algorithms.
   - **Flexible Insertion and Deletion**: Nodes can be easily added or removed without needing to shift other elements, as is necessary in arrays.
2. **Disadvantages**:
   - **Increased Memory Overhead**: Each node requires additional memory for the extra pointer, which can be significant in large lists.
   - **Complex Implementation**: Managing two pointers per node can complicate the implementation and increase the potential for errors, especially during insertion and deletion.

## Section 6. Stacks & Queues

### Stacks

#### Overview of Stacks

A stack is a linear data structure that follows the Last In, **First Out (LIFO)** principle, meaning that the last element added to the stack is the first one to be removed. This structure is analogous to a stack of plates: you can only add or remove the top plate.

#### Key Characteristics of Stacks

1. **Basic Operations**:
   - **Push**: This operation adds an element to the top of the stack.
   - **Pop**: This operation removes the element from the top of the stack and returns it.
   - **Peek** (or Top): This operation retrieves the value of the top element without removing it from the stack.
   - **IsEmpty**: This operation checks whether the stack is empty.
2. Dynamic Size:
   - Stacks can grow and shrink dynamically as elements are added or removed. This flexibility allows for efficient memory usage.
3. Implementation:
   - Stacks can be implemented using arrays or linked lists.
     - **Array-based Stack**: Uses a fixed-size array to store elements. If the stack exceeds its capacity, it may require resizing.
     - **Linked List-based Stack**: Uses nodes to store elements, allowing for dynamic sizing without the need for resizing.
4. Applications:
   - Stacks are widely used in various applications, including:
     - **Function Call Management**: Keeping track of function calls in programming languages (call stack).
     - **Expression Evaluation**: Evaluating mathematical expressions and parsing syntax in compilers.
     - **Backtracking Algorithms**: Managing states in algorithms that require exploring multiple paths, such as maze solving.
5. Performance:
   - The time complexity for push, pop, and peek operations is O(1), making stacks very efficient for these operations.

#### Advantages and disadvantages of Stacks

1. **Advantages**:
   - Simple and easy to implement.
   - Efficient for managing data in a LIFO manner.
   - Useful in various algorithmic applications.
2. **Disadvantages**:
   - Limited access: Only the top element can be accessed directly, which can be a limitation in certain scenarios.
   - Fixed size in array-based implementations can lead to overflow if not managed properly.

### Queues

#### Overview of Queues

A queue is a linear data structure that follows the First In, **First Out (FIFO)** principle, meaning that the first element added to the queue will be the first one to be removed. This structure is analogous to a line of people waiting for service: the person who arrives first is served first.

#### Key Characteristics of Queues

1. **Basic Operations**:
   - **Enqueue**: This operation adds an element to the rear (or back) of the queue.
   - **Dequeue**: This operation removes the element from the front of the queue and returns it.
   - **Peek (or Front)**: This operation retrieves the value of the front element without removing it from the queue.
   - **IsEmpty**: This operation checks whether the queue is empty.
2. **Dynamic Size**:
   - Queues can grow and shrink dynamically as elements are added or removed, allowing for efficient memory usage.
3. **Implementation**:
   - Queues can be implemented using arrays or linked lists.
     - **Array-based Queue**: Uses a fixed-size array to store elements. If the queue exceeds its capacity, it may require resizing or circular implementation to efficiently use space.
     - **Linked List-based Queue**: Uses nodes to store elements, allowing for dynamic sizing without the need for resizing.
4. **Applications**:
   - Queues are widely used in various applications, including:
     - **Task Scheduling**: Managing tasks in operating systems and print spooling.
     - **Breadth-First Search (BFS)**: In graph algorithms, queues help explore nodes level by level.
     - **Buffer Management**: In data streaming and communication systems, queues manage data packets.
5. **Performance**:
   - The time complexity for enqueue and dequeue operations is O(1), making queues very efficient for these operations.

#### Advantages and disadvantages of Queues

1. **Advantages**:
   - Simple and easy to implement.
   - Efficient for managing data in a FIFO manner.
   - Useful in various algorithmic applications.
2. **Disadvantages**:
   - Limited access: Only the front element can be accessed directly, which can be a limitation in certain scenarios.
   - Fixed size in array-based implementations can lead to overflow if not managed properly.

## Section 7. Trees

### Overview of Trees

In computer science, a tree is a hierarchical data structure that consists of nodes connected by edges. It is used to represent relationships between data in a way that allows for efficient searching, insertion, and deletion operations.

### Key Characteristics of Trees

1. **Structure**:
   - A tree consists of a root node, which is the topmost node, and child nodes that branch out from the root. Each node can have zero or more child nodes.
   Nodes that do not have any children are called leaf nodes.
2. **Hierarchy**:
   - Trees are organized in a hierarchical manner, where each node (except the root) has exactly one parent node. This structure allows for a clear representation of relationships.
3. **Types of Trees**:
   - **Binary Tree**: Each node has at most two children, referred to as the left and right child.
   - **Binary Search Tree (BST)**: A binary tree where the left child contains values less than the parent node, and the right child contains values greater than the parent node, allowing for efficient searching.
   - **Balanced Trees**: Such as AVL trees and Red-Black trees, which maintain a balanced height to ensure efficient operations.
   - **N-ary Tree**: A tree where each node can have up to N children.
4. **Traversal Methods**:
   - Trees can be traversed in several ways, including:
     - **Pre-order Traversal**: Visit the root, then recursively visit the left subtree, followed by the right subtree.
     - **In-order Traversal**: Recursively visit the left subtree, visit the root, and then the right subtree (commonly used in BSTs to retrieve sorted data).
     - **Post-order Traversal**: Recursively visit the left subtree, the right subtree, and then the root.
     - **Level-order Traversal**: Visit nodes level by level from top to bottom.
5. **Applications**:
   - Trees are widely used in various applications, including:
     - **File Systems**: Representing directories and files in a hierarchical structure.
     - **Databases**: Indexing data for efficient retrieval.
     - **Artificial Intelligence**: Decision trees for making decisions based on conditions.

### Advantages and disadvantages of Trees

1. **Advantages**:
   - Hierarchical Representation: Trees provide a natural way to represent hierarchical data.
   - Efficient Searching: Especially in binary search trees, where search operations can be performed in O(log n) time on average.
   - Dynamic Size: Trees can grow and shrink dynamically as data is added or removed.
2. **Disadvantages**:
   - Complexity: Implementing and maintaining balanced trees can be complex.
   - Memory Overhead: Each node requires additional memory for pointers to child nodes.

## Section 8. Hash Tables

### Overview of Hash Tables

A hash table is a data structure that stores data in the form of key-value pairs, allowing for efficient data retrieval. It uses a hash function to compute an index (or hash code) into an array of buckets or slots, where the corresponding value can be found. This structure is widely used in applications that require fast access to data, such as implementing dictionaries and maps.

### Key Characteristics of Hash Tables

1. **Keys and Values**:
   - Each entry in a hash table consists of a key and a value. The key is used to uniquely identify the value, allowing for quick lookups.
2. **Hash Function**:
   - A hash function takes a key as input and produces an integer (the hash code) that determines the index in the array where the value will be stored. A good hash function minimizes collisions (when two keys hash to the same index) and distributes keys uniformly across the array.
3. **Buckets**:
   - The array in a hash table is often referred to as buckets. Each bucket can hold one or more entries, especially in cases of collisions. The way collisions are handled can significantly affect the performance of the hash table.

### Collision Resolution Techniques

1. **Chaining**:
   - In this method, each bucket contains a linked list (or another data structure) of all entries that hash to the same index. When a collision occurs, the new entry is simply added to the list in that bucket.
2. **Open Addressing**:
   - This technique involves finding another open slot within the array when a collision occurs. Various probing methods can be used, such as linear probing, quadratic probing, or double hashing.

### Performance

The average time complexity for search, insert, and delete operations in a hash table is O(1), assuming a good hash function and a low load factor (the ratio of the number of entries to the number of buckets). However, in the worst case (e.g., many collisions), the time complexity can degrade to O(n).

### Advantages and disadvantages of Hash Tables

1. **Advantages**:
   - **Fast Access**: Hash tables provide very fast data retrieval, making them ideal for applications requiring quick lookups.
   - **Dynamic Size**: They can grow dynamically as more entries are added, allowing for flexible memory usage.
2. **Disadvantages**:
   - **Collision Handling**: Managing collisions can complicate the implementation and affect performance.
   - **Memory Overhead**: Hash tables may require more memory than other data structures due to the need for buckets and potential empty slots.
   - **Poor Performance with Bad Hash Functions**: If the hash function is poorly designed, it can lead to many collisions, significantly slowing down operations.

## Section 9. Graphs

### Overview of Graphs

A graph is a mathematical structure used to model pairwise relationships between objects. It consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. Graphs are widely used in various fields, including computer science, biology, social sciences, and transportation, to represent and analyze relationships and networks.

### Key Components of Graphs

1. **Vertices (Nodes)**:
   - The fundamental units of a graph, representing entities or objects. For example, in a social network graph, each person can be represented as a vertex.
2. **Edges**:
   - The connections between vertices. Edges can be **directed** (indicating a one-way relationship) or **undirected** (indicating a two-way relationship). For instance, in a directed graph, an edge from vertex A to vertex B indicates a relationship from A to B, but not necessarily from B to A.
3. **Types of Graph**s:
   - **Simple Graph**: A graph without loops (edges connecting a vertex to itself) and multiple edges between the same pair of vertices.
   - **Weighted Graph**: A graph where edges have weights (or costs) associated with them, often used to represent distances or costs in networks.
   - **Cyclic Graph**: A graph that contains at least one cycle (a path that starts and ends at the same vertex).
   - **Acyclic Graph**: A graph that does not contain any cycles.
   - **Connected Graph**: A graph in which there is a path between every pair of vertices.
   - **Disconnected Graph**: A graph that has at least two vertices with no path connecting them.
4. **Graph Representation**:
   - Graphs can be represented in various ways, including:
     - **Adjacency Matrix**: A 2D array where the element at row i and column j indicates the presence (and possibly the weight) of an edge between vertices i and j.
     - **Adjacency List**: A collection of lists or arrays where each list corresponds to a vertex and contains the vertices that are adjacent to it.

### Applications of Graphs

   - Graphs have numerous applications across different domains, including:
     - **Social Networks**: Modeling relationships between individuals or organizations.
     - **Transportation Networks**: Representing routes and connections in road systems, flight paths, or public transit.
     - **Computer Networks**: Analyzing connections between computers, routers, and servers.
     - **Biological Networks**: Understanding interactions between genes, proteins, or species.
     - **Recommendation Systems**: Using graphs to model user preferences and item relationships.

### Algorithms of Graphs

   - Several algorithms are commonly used to analyze and manipulate graphs, including:
     - **Depth-First Search (DFS)**: An algorithm for traversing or searching through a graph by exploring as far as possible along each branch before backtracking.
     - **Breadth-First Search (BFS)**: An algorithm for traversing or searching through a graph level by level, exploring all neighbors of a vertex before moving to the next level.
     - **Dijkstra's Algorithm**: An algorithm for finding the shortest path between nodes in a weighted graph.
     - **Kruskal's and Prim's Algorithms**: Algorithms for finding the minimum spanning tree of a graph.

