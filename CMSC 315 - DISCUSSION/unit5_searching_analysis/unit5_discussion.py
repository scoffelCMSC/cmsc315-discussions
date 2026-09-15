"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # A linear search looks through every item and assumes the list is unsorted. Therefore, its complexity is O(n).
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    # Similar approach to the methods used in the lab, based on our ZyBooks readings this week.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Each iteration divides the search space in half, following O(log n).
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2 # Midpoint
        # High end of the current search space
        if lst[mid] < target:
            low = mid + 1
        # Low end of the current search space
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Starting data set. A small grouping of numbers that follow a user's selected username.
    id = [1001, 1003, 1008, 1010, 1027]
    print(f"User ID: {id}")

    # Search for ID at certain index that exists.  (Existing value search)
    print("Does a user have ID 1003?")
    # Index 1 should be returned for both searches.
    print(f"Linear Search: {linear_search(id, 1003)}")
    print(f"Binary Search: {binary_search(id, 1003)}")

    # Searching for an ID that doesn't exist (Non-existing value search)
    print("Does a user have ID 1002?")
    # -1 should be returned for there being no index.
    print(f"Linear Search: {linear_search(id, 1002)}")
    print(f"Binary Search: {binary_search(id, 1002)}")

    print("1003 should be found, and 1002 should not be found and return -1.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Create a very large list. Save some sanity and make the code cleaner by using range.
    big_id = list(range(1000, 9999))
    print("This list contains all possible valid user IDs, from 1000 to 9999.")

    # In-list ID search should return proper index. 
    print("Can a user use the ID 8832?")
    # Perform both searches, should return an existing index for both.
    print(f"Linear Search: {linear_search(big_id, 8832)}")
    print(f"Binary Search: {binary_search(big_id, 8832)}")

    # Out of list ID should return -1 because it's not in the list.
    print("Can a user use the ID 999?")
    # Perform both searches to return -1.
    # Linear still searches the whole list for the ID, as it assumes the list is not sorted.
    print(f"Linear Search: {linear_search(big_id, 999)}")
    print(f"Binary Search: {binary_search(big_id, 999)}")

    print("Both search instances should produce the same result in their comparisons, the difference is the method.")
    print("A linear search for the first ID needs to check 7833 different indexes, and a binary search runs 13 comparisons.")
    print("If the list is sorted, binary search is more optimized.")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Empty List Test
    print("Edge Case: Empty List")
    print("Both searches should return -1.")
    empty_list = []
    print(f"Linear Search: {linear_search(empty_list, 74)}")
    print(f"Binary Search: {binary_search(empty_list, 74)}")

    # One Element List
    print("Edge Case: Single Element List")
    print("First check will check for the single element.")
    single_list = [658]
    # Check for present element
    print(f"Linear Search: {linear_search(single_list, 658)}")
    print(f"Binary Search: {binary_search(single_list, 658)}")
    print("Both searches should return 0.")
    # Check for a non-present element
    print(f"Linear Search: {linear_search(single_list, 888)}")
    print(f"Binary Search: {binary_search(single_list, 888)}")
    print("Both searches should return -1.")


if __name__ == "__main__":
    main()