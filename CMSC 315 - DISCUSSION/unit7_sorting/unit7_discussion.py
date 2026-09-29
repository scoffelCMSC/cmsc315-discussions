"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Create the list copy
    dupe_list = lst.copy()
    n = len(dupe_list)

    # Outer loop will run for each pass through the list
    for i in range(n):
        # Inner loop performs comaprisons on adjacent elements to perform swaps.
        for j in range(n - 1):
            if dupe_list[j] > dupe_list[j + 1]:
                dupe_list[j], dupe_list[j + 1] = dupe_list[j + 1], dupe_list[j]
    return dupe_list



def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1:
        return lst
    # Split the list
    midpoint = len(lst) // 2
    left_side = lst[:midpoint]
    right_side = lst[midpoint:]
    # Recursively call both left and right to be sorted
    left_sort = merge_sort(left_side)
    right_sort = merge_sort(right_side)
    # Return the merged result
    return merge(left_sort, right_sort)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    combined = []
    # Track both left and right index positions
    l_index = 0
    r_index = 0
    # Loop through both lists as long as comparable elements are present
    while l_index < len(left) and r_index < len(right):
        # Move from left to right, observe size of the element to determine whether it is put in the left or right.
        if left[l_index] <= right[r_index]:
            combined.append(left[l_index])
            l_index += 1
        else:
            combined.append(right[r_index])
            r_index += 1
    # Append remaining elements from the sublists.
    combined.extend(left[l_index:])
    combined.extend(right[r_index:])

    return combined

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values. (Order Numbers)
    # 2. Display the original list. (Print Statement)
    # 3. Sort the list using Bubble Sort. (Perform sort)
    # 4. Sort the same list using Merge Sort. (Perform sort 2)
    # 5. Clearly label and display all results. (Make it neat)

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    order_no = [1787, 5503, 3552, 2264, 7457, 3460, 1127, 6693, 3346]

    print(f"\nStarting Order List: {order_no}")
    print(f"Bubble Sorted List: {bubble_sort(order_no)}")
    print(f"Merge Sorted List: {merge_sort(order_no)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    # Set 2 uses strings for data instead.
    item_name = ["Chair", "Sand", "Filter", "Batteries", "Glue", "Xylophone", "Cup"]

    print(f"\nStarting Order List: {item_name}")
    print(f"Bubble Sorted List: {bubble_sort(item_name)}")
    print(f"Merge Sorted List: {merge_sort(item_name)}")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Bubble sort needs to iterate through all elements during sorting to perform swaps. 
    # Swaps do not occur when a value equal to another element is encountered.
    # Merge Sort proceeds as normal due to <= and allows the duplicate vlaue to be placed next when sorting.
    print("\nEdge Case 1")
    dupe_list = [44, 986057459, 2, 44, 986057458, 354, 777]
    print(f"Duplicate Value List: {dupe_list}")
    print(f"Dupe Bubble Sort: {bubble_sort(dupe_list)}")
    print(f"Dupe Merge Sort: {merge_sort(dupe_list)}")

    print("\nEdge Case 2")
    # When proceeding through a list with sorted elements, swaps do not occur during iterations for Bubble Sort.
    # Merge Sort also still splits the list down and re-merges it. 
    # As such, performance does not improve for either. It simply takes another path.
    sorted_list = [12, 17, 18, 20, 30, 300, 477, 478]
    print(f"Sorted Value List: {sorted_list}")
    print(f"Sorted Bubble Sort: {bubble_sort(sorted_list)}")
    print(f"Sorted Merge Sort: {merge_sort(sorted_list)}")

if __name__ == "__main__":
    main()