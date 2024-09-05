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

1. **Linear Growth**: In an O(n) algorithm, if the input size doubles, the time taken to execute the algorithm also approximately doubles. This is because each element in the input must be processed individually.
2. **Common Examples**:
   - **Linear Search**: Searching for an element in an unsorted list requires checking each element until the desired one is found, resulting in O(n) complexity.
   - **Iterating Through a List**: Any operation that involves going through each element of a list or array, such as summing the elements or finding the maximum value, typically has O(n) complexity.

#### Practical Implications

1. **Scalability**: Algorithms with O(n) complexity are generally efficient for moderate input sizes. However, as the input size grows significantly, the performance may still become a concern, especially compared to algorithms with better complexities (like O(log n) or O(1)).
2. **Real-World Applications**: Understanding O(n) is crucial for developers when designing algorithms, as it helps in making informed decisions about which algorithms to use based on the expected size of the input data.

