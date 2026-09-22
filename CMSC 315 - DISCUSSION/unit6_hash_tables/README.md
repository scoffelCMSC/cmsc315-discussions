# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
In this assignment I was able to learn more about how dictionaries and hash codes are intertwined and their uses in efficiently locating items. I have worked with dictionaries before but I have never looked too much into the internal works- I found this assignment and unit incredibly fascinating.
2. What challenges did you encounter, and how did you overcome them?
During this assignment I mostly struggled still with understanding how hashes themselves worked, however seeing what they do and how they accomplish it helped make it much simpler. 
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
Hash tables store data in a key-value pair with the utilization of a map ADT. A key is passed through the hash function to identify where it can be stored. The usage of algorithms keeps searches down where one would have to traverse a tree. This results in their average time complexity only being O(1). Collision happens when the hash table calculates the same index for two separate keys. Collisions adversely can decrease effiency, as the worst case becomes O(n) depending on the number of collisions so that the collisions are resolved.