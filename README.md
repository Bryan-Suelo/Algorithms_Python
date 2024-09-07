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

O(log n), known as logarithmic time complexity, indicates that the execution time of an algorithm increases logarithmically as the input size (n) increases.

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
   - In formal terms, an algorithm is said to have O(log n) complexity if the number of operations required to complete the algorithm can be expressed as a logarithmic function of the input size. The base of the logarithm is typically 2, reflecting the binary nature of many algorithms that exhibit this complexity