# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
Fir this assignment, I was able to practice recursion further which I had been struggling with last week. I was able to find some simpler list implementations to not have to make an aggressively long list or create a csv file to be read using big_id = list(range(1000, 9999)). It was incredibly interesting to implement the different search methods and understand better how the algorithms in our reading functioned.
2. What challenges did you encounter, and how did you overcome them?
My main challenge this week was the translation, however this time to overcome it I was able to compare the implementation closer in the lab to what I would need to do for Python. I took a bit longer to wrap my head around the algorithms and how they worked in implementation, but once I figured it out I was able to understand what I was doing instead of following along blindly to the implementations showcased in our readings.
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
A binary search is able to accomplish the location of an index in significantly fewer steps in most cases compared to linear searches by cutting the search space in half with every iteration. However, in order to do this a binary search requires the list to be sorted in some form of highest to lowest or vice versa. For example, if employee IDs are ordered in numerical order in a database and there are hundreds present, searching for a specific ID would be signficantly shorter. When that list is not sorted, a linear search would be used instead. Say that the employees are sorted in alphabetical order, so the IDs are put into the array in an unsorted manner. A linear search would have no problem getting to the requested item or index, as linear searches inherently assume that a list is not sorted. 