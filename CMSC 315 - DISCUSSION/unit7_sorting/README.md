# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
During this assignment I was able to get a much more firm grasp on how bubble and merge sorts are implemented, especially in Python. Merge Sort particularly vexed me for its complexity, but like many things, it boils down to simplification.
2. What challenges did you encounter, and how did you overcome them?
My main issue stemmed from my understanding of how merge sort functioned. While its concept of splitting down into smaller parts made sense to me, its implementation proved more difficult as I struggled to understand how its splitting occured recursively. The practice that some of these discussions have given me with recursion has assisted me immensely.
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.
Bubble Sort is a simple and easier to understand algorithm compared to Merge Sort. It compares neighboring values throughought a list as it moves along, giving it a runtime complexity of O(n^2). Due to its operation of moving down a list as such, it is inefficient for larger data sets. Merge Sort fills that gap better by splitting the list into smaller parts to sort before remerging them. The complexity as such for runtime is O(n log n). While it functions better for lerger lists, it costs more resources to utilize and is not as resource efficient for smaller lists.